for(let q of arguments){let t=0,a=q.replace(/-/g,'');for(let i=0;i<a.length;i++)t+=parseInt(a[i])*(10-i);let d=(11-(t%11))%11;print(q+(d==10?'X':d))}
