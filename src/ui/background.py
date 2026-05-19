"""Neural background animation + SVG favicon — injected into parent document."""

import streamlit.components.v1 as components


def render_neural_background():
    components.html(
        """
<script>
(function() {
    var doc = window.parent.document;
    var win = window.parent;

    // ── Persistent hide CSS — survives Streamlit page transitions ──
    if (!doc.getElementById('as-global-hide')) {
        var hide = doc.createElement('style');
        hide.id = 'as-global-hide';
        hide.textContent = [
            '[data-testid="stSidebar"]{display:none!important;}',
            '[data-testid="stSidebarCollapsedControl"]{display:none!important;}',
            '[data-testid="stSidebarCollapseButton"]{display:none!important;}',
            '[data-testid="stExpandSidebarButton"]{display:none!important;}',
            'section[data-testid="stSidebarContent"]{display:none!important;}',
            'header[data-testid="stHeader"]{display:none!important;}',
        ].join('');
        doc.head.appendChild(hide);
    }

    // ── SVG favicon ──
    doc.querySelectorAll('link[rel*="icon"]').forEach(function(l) { l.remove(); });
    var fav = doc.createElement('link');
    fav.rel = 'icon';
    fav.type = 'image/svg+xml';
    fav.href = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"%3E%3Cpath d="M16 2L4 8v10c0 8 5.5 13.5 12 16 6.5-2.5 12-8 12-16V8L16 2z" fill="%23D97757" opacity="0.9"/%3E%3Cpath d="M13.5 17.5l-3-3-1.5 1.5 4.5 4.5 9-9-1.5-1.5z" fill="white"/%3E%3C/svg%3E';
    doc.head.appendChild(fav);

    // ── Neural animation — inject as native <script> in parent <head> ──
    // Runs in parent window scope; survives iframe destruction on page nav.
    if (doc.getElementById('as-neural-script')) return;

    var canvas = doc.createElement('canvas');
    canvas.id = 'as-neural-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;';
    doc.body.insertBefore(canvas, doc.body.firstChild);

    var script = doc.createElement('script');
    script.id = 'as-neural-script';
    script.textContent = '(function(){'
        + 'var CW=730,N=30,MD=190,SP=0.22,nodes=[];'
        + 'function mkCanvas(){'
        + '  var c=document.getElementById("as-neural-canvas");'
        + '  if(!c){c=document.createElement("canvas");c.id="as-neural-canvas";'
        + '    c.style.cssText="position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;";'
        + '    document.body.insertBefore(c,document.body.firstChild);}'
        + '  c.width=window.innerWidth;c.height=window.innerHeight;return c;'
        + '}'
        + 'var c0=mkCanvas();'
        + 'window.addEventListener("resize",function(){var c=document.getElementById("as-neural-canvas");if(c){c.width=window.innerWidth;c.height=window.innerHeight;}});'
        + 'for(var i=0;i<N;i++){'
        + '  var s=i<N/2?"left":"right",sw=Math.max((c0.width-CW)/2,80);'
        + '  nodes.push({x:s==="left"?Math.random()*sw:c0.width-Math.random()*sw,'
        + '    y:Math.random()*c0.height,vx:(Math.random()-0.5)*SP,vy:(Math.random()-0.5)*SP,'
        + '    r:2+Math.random()*2.5,pulse:Math.random()*Math.PI*2,side:s});'
        + '}'
        + 'function draw(){'
        + '  var c=document.getElementById("as-neural-canvas");'
        + '  if(!c)c=mkCanvas();'
        + '  var ctx=c.getContext("2d");'
        + '  ctx.clearRect(0,0,c.width,c.height);'
        + '  var lm=(c.width-CW)/2+24,rm=(c.width+CW)/2-24;'
        + '  for(var k=0;k<nodes.length;k++){'
        + '    var n=nodes[k];n.x+=n.vx;n.y+=n.vy;n.pulse+=0.012;'
        + '    if(n.y<0){n.y=0;n.vy=Math.abs(n.vy);}if(n.y>c.height){n.y=c.height;n.vy=-Math.abs(n.vy);}'
        + '    if(n.x<0){n.x=0;n.vx=Math.abs(n.vx);}if(n.x>c.width){n.x=c.width;n.vx=-Math.abs(n.vx);}'
        + '    if(n.side==="left"&&n.x>lm)n.vx=-Math.abs(n.vx);'
        + '    if(n.side==="right"&&n.x<rm)n.vx=Math.abs(n.vx);'
        + '  }'
        + '  for(var i=0;i<nodes.length;i++){for(var j=i+1;j<nodes.length;j++){'
        + '    var dx=nodes[i].x-nodes[j].x,dy=nodes[i].y-nodes[j].y,d=Math.sqrt(dx*dx+dy*dy);'
        + '    if(d<MD){ctx.beginPath();ctx.moveTo(nodes[i].x,nodes[i].y);ctx.lineTo(nodes[j].x,nodes[j].y);'
        + '      ctx.strokeStyle="rgba(217,119,87,"+((1-d/MD)*0.22)+")";ctx.lineWidth=1;ctx.stroke();}'
        + '  }}'
        + '  for(var m=0;m<nodes.length;m++){'
        + '    var nd=nodes[m],p=0.5+0.5*Math.sin(nd.pulse);'
        + '    ctx.beginPath();ctx.arc(nd.x,nd.y,nd.r+p*0.8,0,Math.PI*2);'
        + '    ctx.fillStyle="rgba(217,119,87,"+(0.38+0.18*p)+")";ctx.fill();'
        + '  }'
        + '  requestAnimationFrame(draw);'
        + '}'
        + 'requestAnimationFrame(draw);'
        + '})();';
    doc.head.appendChild(script);
})();
</script>
""",
        height=0,
        scrolling=False,
    )
