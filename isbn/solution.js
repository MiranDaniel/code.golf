for(q of arguments){t=0,a=q.replace(/-/g,'');for(i=0;i<a.length;i++)t+=parseInt(a[i])*(10-i);d=(11-(t%11))%11;print(q+(d==10?'X':d))}
