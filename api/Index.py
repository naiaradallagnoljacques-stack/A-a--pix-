from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Acai do Ponto</title>
<style>body{font-family:sans-serif;margin:0;background:#f8f0ff}.header{background:#4a148c;color:white;padding:30px;text-align:center}.box{max-width:420px;margin:auto;padding:15px}.card{background:white;border-radius:20px;padding:20px;margin-top:-25px;box-shadow:0 8px 20px rgba(0,0,0,.15)}img{width:100%;border-radius:14px}.preco{font-size:32px;font-weight:900;color:#4a148c}.btn{display:block;padding:18px;border-radius:12px;text-align:center;text-decoration:none;font-weight:900;margin-top:14px;font-size:18px}.zap{background:#25D366;color:white}.pix{background:#4a148c;color:white}.pix-box{background:#f3e5f5;padding:15px;border-radius:12px;margin-top:15px;text-align:center;display:none}</style>
</head><body>
<div class="header"><h1>Acai do Ponto</h1><p>Alegrete - Entrega 30min</p></div>
<div class="box"><div class="card">
<img src="https://images.unsplash.com/photo-1587314168485-3236d6710814">
<h2>Acai 500ml - R$ 22,00</h2>
<a class="btn pix" href="#" onclick="document.getElementById('pixbox').style.display='block';return false;">PAGAR COM PIX</a>
<div id="pixbox" class="pix-box"><p>Chave PIX:</p><h2 id="chave">99292670000</h2><p>Nome: Claudia Silva</p>
<button onclick="navigator.clipboard.writeText(document.getElementById('chave').innerText);alert('Copiado!')" style="padding:12px;background:#4a148c;color:white;border:none;border-radius:8px;font-weight:bold">COPIAR CHAVE PIX</button><br><br>
<a class="btn zap" href="https://wa.me/55991600621">JA PAGUEI, ENVIAR COMPROVANTE</a></div>
<a class="btn zap" href="https://wa.me/55991600621">PEDIR NO WHATSAPP</a>
</div></div></body></html>
"""
@app.route('/')
def home():
    return render_template_string(HTML)
