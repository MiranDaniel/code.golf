a=0;while(a<10001){if(a%[...''+a].reduce((s,n)=>+n+s,0)<1)print(a);a+=1}