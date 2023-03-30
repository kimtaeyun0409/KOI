fc=79e9; % 동작 carrier 주파수
c=3e8; % 빛의 속도
lambda=c/fc; % 파장 [m]

range_max=150; % 레이더 동작 최대 거리 [m]

%레이더 스윕시간은 최대 이동거리의 Round trip 시간에 최소 5.5배는 되어야 한다.
%150m 거리라면 5.5usec 이상의 스윕 시간이 필요하고 우리는 1msec을 할 것이니.... 
%스윕 타임에 문제는 전혀 없을 것으로 생각

tm_min=5.5*range2time(range_max,c);
%우리는 tm을 1msec로 셋팅하겠습니다.
tm=1e-3;
bw=4e9; %시스템 대역폭입니다.
range_res=bw2range(bw); %계산된 Range 죠
sweep_slope=bw/tm; % 스윕 time 이죠

fr_max=range2beat(range_max,sweep_slope,c); %max 거리와 제안된 chirp 속도에 의한 max bit frequency

v_max=0; %여기서 입력하는 숫자는 km/hour입니다.
v_max_mps=v_max*1000/3600; % 이렇게 속도를 m/sec로 바꿔 줘야죠.

fd_max=speed2dop(2*v_max_mps, lambda); % 도플러 때문에 발생하는 주파수 shift max 값은
fb_max=fr_max+fd_max; %최대 비트 주파수는 chirp에 의한 것과 도플러에 의한 것의 합

fs=max(2*fb_max,bw); % 최대 beat 주파수의 2배를 샘플링 주파수로 잡겠습니다.
% 아래 셋팅은 linear Saw 모양의 Up Chirp을 의미한다.
waveform=phased.FMCWWaveform('SweepTime',tm,'SweepBandwidth',bw,'SampleRate',fs);
%이제 Plot을 좀 해 볼까요!!!

sig=waveform();
subplot(211); plot(0:1/fs:tm-1/fs,real(sig));
xlabel('Time(s)'); ylabel('Amplfitude (v)');
title('FMCW Signal'); axis tight;
subplot(212); spectrogram(sig,32,16,32,fs,'yaxis');
title('FMCW signal spectrogram');






