from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io
import base64
import os

app = Flask(__name__)
CORS(app)

def decode_base64_image(image_base64):
    image_data = base64.b64decode(image_base64)
    return Image.open(io.BytesIO(image_data))

def encode_image_to_base64(image):
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return base64.b64encode(img_io.getvalue()).decode('utf-8')

def encode_image_to_base64_format(image, format):
    img_io = io.BytesIO()
    
    # Verificar se o formato é JPEG e a imagem tem um canal alfa (transparência)
    if format.upper() == 'JPEG' and image.mode == 'RGBA':
        image = image.convert('RGB')
    
    image.save(img_io, format)
    img_io.seek(0)
    return base64.b64encode(img_io.getvalue()).decode('utf-8')

def handle_image_processing(image_base64, process_function):
    try:
        image = decode_base64_image(image_base64)
        image = process_function(image)
        processed_image_base64 = encode_image_to_base64(image)
        return jsonify({'processed_image': processed_image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html><html><head>
          <title>help</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
          
          
          
          
          
          <style>
          code[class*=language-],pre[class*=language-]{color:#333;background:0 0;font-family:Consolas,"Liberation Mono",Menlo,Courier,monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.4;-moz-tab-size:8;-o-tab-size:8;tab-size:8;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none}pre[class*=language-]{padding:.8em;overflow:auto;border-radius:3px;background:#f5f5f5}:not(pre)>code[class*=language-]{padding:.1em;border-radius:.3em;white-space:normal;background:#f5f5f5}.token.blockquote,.token.comment{color:#969896}.token.cdata{color:#183691}.token.doctype,.token.macro.property,.token.punctuation,.token.variable{color:#333}.token.builtin,.token.important,.token.keyword,.token.operator,.token.rule{color:#a71d5d}.token.attr-value,.token.regex,.token.string,.token.url{color:#183691}.token.atrule,.token.boolean,.token.code,.token.command,.token.constant,.token.entity,.token.number,.token.property,.token.symbol{color:#0086b3}.token.prolog,.token.selector,.token.tag{color:#63a35c}.token.attr-name,.token.class,.token.class-name,.token.function,.token.id,.token.namespace,.token.pseudo-class,.token.pseudo-element,.token.url-reference .token.variable{color:#795da3}.token.entity{cursor:help}.token.title,.token.title .token.punctuation{font-weight:700;color:#1d3e81}.token.list{color:#ed6a43}.token.inserted{background-color:#eaffea;color:#55a532}.token.deleted{background-color:#ffecec;color:#bd2c00}.token.bold{font-weight:700}.token.italic{font-style:italic}.language-json .token.property{color:#183691}.language-markup .token.tag .token.punctuation{color:#333}.language-css .token.function,code.language-css{color:#0086b3}.language-yaml .token.atrule{color:#63a35c}code.language-yaml{color:#183691}.language-ruby .token.function{color:#333}.language-markdown .token.url{color:#795da3}.language-makefile .token.symbol{color:#795da3}.language-makefile .token.variable{color:#183691}.language-makefile .token.builtin{color:#0086b3}.language-bash .token.keyword{color:#0086b3}pre[data-line]{position:relative;padding:1em 0 1em 3em}pre[data-line] .line-highlight-wrapper{position:absolute;top:0;left:0;background-color:transparent;display:block;width:100%}pre[data-line] .line-highlight{position:absolute;left:0;right:0;padding:inherit 0;margin-top:1em;background:hsla(24,20%,50%,.08);background:linear-gradient(to right,hsla(24,20%,50%,.1) 70%,hsla(24,20%,50%,0));pointer-events:none;line-height:inherit;white-space:pre}pre[data-line] .line-highlight:before,pre[data-line] .line-highlight[data-end]:after{content:attr(data-start);position:absolute;top:.4em;left:.6em;min-width:1em;padding:0 .5em;background-color:hsla(24,20%,50%,.4);color:#f4f1ef;font:bold 65%/1.5 sans-serif;text-align:center;vertical-align:.3em;border-radius:999px;text-shadow:none;box-shadow:0 1px #fff}pre[data-line] .line-highlight[data-end]:after{content:attr(data-end);top:auto;bottom:.4em}html body{font-family:'Helvetica Neue',Helvetica,'Segoe UI',Arial,freesans,sans-serif;font-size:16px;line-height:1.6;color:#333;background-color:#fff;overflow:initial;box-sizing:border-box;word-wrap:break-word}html body>:first-child{margin-top:0}html body h1,html body h2,html body h3,html body h4,html body h5,html body h6{line-height:1.2;margin-top:1em;margin-bottom:16px;color:#000}html body h1{font-size:2.25em;font-weight:300;padding-bottom:.3em}html body h2{font-size:1.75em;font-weight:400;padding-bottom:.3em}html body h3{font-size:1.5em;font-weight:500}html body h4{font-size:1.25em;font-weight:600}html body h5{font-size:1.1em;font-weight:600}html body h6{font-size:1em;font-weight:600}html body h1,html body h2,html body h3,html body h4,html body h5{font-weight:600}html body h5{font-size:1em}html body h6{color:#5c5c5c}html body strong{color:#000}html body del{color:#5c5c5c}html body a:not([href]){color:inherit;text-decoration:none}html body a{color:#08c;text-decoration:none}html body a:hover{color:#00a3f5;text-decoration:none}html body img{max-width:100%}html body>p{margin-top:0;margin-bottom:16px;word-wrap:break-word}html body>ol,html body>ul{margin-bottom:16px}html body ol,html body ul{padding-left:2em}html body ol.no-list,html body ul.no-list{padding:0;list-style-type:none}html body ol ol,html body ol ul,html body ul ol,html body ul ul{margin-top:0;margin-bottom:0}html body li{margin-bottom:0}html body li.task-list-item{list-style:none}html body li>p{margin-top:0;margin-bottom:0}html body .task-list-item-checkbox{margin:0 .2em .25em -1.8em;vertical-align:middle}html body .task-list-item-checkbox:hover{cursor:pointer}html body blockquote{margin:16px 0;font-size:inherit;padding:0 15px;color:#5c5c5c;background-color:#f0f0f0;border-left:4px solid #d6d6d6}html body blockquote>:first-child{margin-top:0}html body blockquote>:last-child{margin-bottom:0}html body hr{height:4px;margin:32px 0;background-color:#d6d6d6;border:0 none}html body table{margin:10px 0 15px 0;border-collapse:collapse;border-spacing:0;display:block;width:100%;overflow:auto;word-break:normal;word-break:keep-all}html body table th{font-weight:700;color:#000}html body table td,html body table th{border:1px solid #d6d6d6;padding:6px 13px}html body dl{padding:0}html body dl dt{padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:700}html body dl dd{padding:0 16px;margin-bottom:16px}html body code{font-family:Menlo,Monaco,Consolas,'Courier New',monospace;font-size:.85em;color:#000;background-color:#f0f0f0;border-radius:3px;padding:.2em 0}html body code::after,html body code::before{letter-spacing:-.2em;content:'\00a0'}html body pre>code{padding:0;margin:0;word-break:normal;white-space:pre;background:0 0;border:0}html body .highlight{margin-bottom:16px}html body .highlight pre,html body pre{padding:1em;overflow:auto;line-height:1.45;border:#d6d6d6;border-radius:3px}html body .highlight pre{margin-bottom:0;word-break:normal}html body pre code,html body pre tt{display:inline;max-width:initial;padding:0;margin:0;overflow:initial;line-height:inherit;word-wrap:normal;background-color:transparent;border:0}html body pre code:after,html body pre code:before,html body pre tt:after,html body pre tt:before{content:normal}html body blockquote,html body dl,html body ol,html body p,html body pre,html body ul{margin-top:0;margin-bottom:16px}html body kbd{color:#000;border:1px solid #d6d6d6;border-bottom:2px solid #c7c7c7;padding:2px 4px;background-color:#f0f0f0;border-radius:3px}@media print{html body{background-color:#fff}html body h1,html body h2,html body h3,html body h4,html body h5,html body h6{color:#000;page-break-after:avoid}html body blockquote{color:#5c5c5c}html body pre{page-break-inside:avoid}html body table{display:table}html body img{display:block;max-width:100%;max-height:100%}html body code,html body pre{word-wrap:break-word;white-space:pre}}.markdown-preview{width:100%;height:100%;box-sizing:border-box}.markdown-preview ul{list-style:disc}.markdown-preview ul ul{list-style:circle}.markdown-preview ul ul ul{list-style:square}.markdown-preview ol{list-style:decimal}.markdown-preview ol ol,.markdown-preview ul ol{list-style-type:lower-roman}.markdown-preview ol ol ol,.markdown-preview ol ul ol,.markdown-preview ul ol ol,.markdown-preview ul ul ol{list-style-type:lower-alpha}.markdown-preview .newpage,.markdown-preview .pagebreak{page-break-before:always}.markdown-preview pre.line-numbers{position:relative;padding-left:3.8em;counter-reset:linenumber}.markdown-preview pre.line-numbers>code{position:relative}.markdown-preview pre.line-numbers .line-numbers-rows{position:absolute;pointer-events:none;top:1em;font-size:100%;left:0;width:3em;letter-spacing:-1px;border-right:1px solid #999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.markdown-preview pre.line-numbers .line-numbers-rows>span{pointer-events:none;display:block;counter-increment:linenumber}.markdown-preview pre.line-numbers .line-numbers-rows>span:before{content:counter(linenumber);color:#999;display:block;padding-right:.8em;text-align:right}.markdown-preview .mathjax-exps .MathJax_Display{text-align:center!important}.markdown-preview:not([data-for=preview]) .code-chunk .code-chunk-btn-group{display:none}.markdown-preview:not([data-for=preview]) .code-chunk .status{display:none}.markdown-preview:not([data-for=preview]) .code-chunk .output-div{margin-bottom:16px}.markdown-preview .md-toc{padding:0}.markdown-preview .md-toc .md-toc-link-wrapper .md-toc-link{display:inline;padding:.25rem 0}.markdown-preview .md-toc .md-toc-link-wrapper .md-toc-link div,.markdown-preview .md-toc .md-toc-link-wrapper .md-toc-link p{display:inline}.markdown-preview .md-toc .md-toc-link-wrapper.highlighted .md-toc-link{font-weight:800}.scrollbar-style::-webkit-scrollbar{width:8px}.scrollbar-style::-webkit-scrollbar-track{border-radius:10px;background-color:transparent}.scrollbar-style::-webkit-scrollbar-thumb{border-radius:5px;background-color:rgba(150,150,150,.66);border:4px solid rgba(150,150,150,.66);background-clip:content-box}html body[for=html-export]:not([data-presentation-mode]){position:relative;width:100%;height:100%;top:0;left:0;margin:0;padding:0;overflow:auto}html body[for=html-export]:not([data-presentation-mode]) .markdown-preview{position:relative;top:0;min-height:100vh}@media screen and (min-width:914px){html body[for=html-export]:not([data-presentation-mode]) .markdown-preview{padding:2em calc(50% - 457px + 2em)}}@media screen and (max-width:914px){html body[for=html-export]:not([data-presentation-mode]) .markdown-preview{padding:2em}}@media screen and (max-width:450px){html body[for=html-export]:not([data-presentation-mode]) .markdown-preview{font-size:14px!important;padding:1em}}@media print{html body[for=html-export]:not([data-presentation-mode]) #sidebar-toc-btn{display:none}}html body[for=html-export]:not([data-presentation-mode]) #sidebar-toc-btn{position:fixed;bottom:8px;left:8px;font-size:28px;cursor:pointer;color:inherit;z-index:99;width:32px;text-align:center;opacity:.4}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] #sidebar-toc-btn{opacity:1}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc{position:fixed;top:0;left:0;width:300px;height:100%;padding:32px 0 48px 0;font-size:14px;box-shadow:0 0 4px rgba(150,150,150,.33);box-sizing:border-box;overflow:auto;background-color:inherit}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar{width:8px}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar-track{border-radius:10px;background-color:transparent}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar-thumb{border-radius:5px;background-color:rgba(150,150,150,.66);border:4px solid rgba(150,150,150,.66);background-clip:content-box}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc a{text-decoration:none}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc .md-toc{padding:0 16px}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc .md-toc .md-toc-link-wrapper .md-toc-link{display:inline;padding:.25rem 0}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc .md-toc .md-toc-link-wrapper .md-toc-link div,html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc .md-toc .md-toc-link-wrapper .md-toc-link p{display:inline}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc .md-toc .md-toc-link-wrapper.highlighted .md-toc-link{font-weight:800}html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{left:300px;width:calc(100% - 300px);padding:2em calc(50% - 457px - 300px / 2);margin:0;box-sizing:border-box}@media screen and (max-width:1274px){html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{padding:2em}}@media screen and (max-width:450px){html body[for=html-export]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{width:100%}}html body[for=html-export]:not([data-presentation-mode]):not([html-show-sidebar-toc]) .markdown-preview{left:50%;transform:translateX(-50%)}html body[for=html-export]:not([data-presentation-mode]):not([html-show-sidebar-toc]) .md-sidebar-toc{display:none}
    /* Please visit the URL below for more information: */
    /*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */
    
          </style>
          <!-- The content below will be included at the end of the <head> element. --><script type="text/javascript">
      document.addEventListener("DOMContentLoaded", function () {
        // your code here
      });
    </script></head><body for="html-export">
        
        
          <div class="crossnote markdown-preview  ">
          
    <h1 id="api-documentation">API Documentation </h1>
    <h2 id="endpoints">Endpoints </h2>
    <h3 id="get-">GET / </h3>
    <p><strong>Description</strong>: Home page.</p>
    <p><strong>Method</strong>: <code>GET</code></p>
    <p><strong>Request URL</strong>: <code>/</code></p>
    <h3 id="post-resize">POST /resize </h3>
    <p><strong>Description</strong>: Resize image.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/resize</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span><span class="token punctuation">,</span>
      <span class="token property">"width"</span><span class="token operator">:</span> &lt;new_width&gt;<span class="token punctuation">,</span>
      <span class="token property">"height"</span><span class="token operator">:</span> &lt;new_height&gt;
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-grayscale">POST /grayscale </h3>
    <p><strong>Description</strong>: Convert image to grayscale.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/grayscale</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-no_transparency">POST /no_transparency </h3>
    <p><strong>Description</strong>: Remove transparency from image.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/no_transparency</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-sprite_txt">POST /sprite_txt </h3>
    <p><strong>Description</strong>: Convert image to text representation.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/sprite_txt</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-negative">POST /negative </h3>
    <p><strong>Description</strong>: Convert image to negative.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/negative</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-black_white">POST /black_white </h3>
    <p><strong>Description</strong>: Convert image to black and white.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/black_white</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-convert">POST /convert </h3>
    <p><strong>Description</strong>: Convert image format.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/convert</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span><span class="token punctuation">,</span>
      <span class="token property">"format"</span><span class="token operator">:</span> <span class="token string">"&lt;new_format&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><p><strong>Note</strong>: <code>&lt;new_format&gt;</code> can be <code>JPG</code>, <code>PNG</code>, <code>BMP</code>, or <code>GIF</code>.</p>
    <h3 id="post-dimensions">POST /dimensions </h3>
    <p><strong>Description</strong>: Get image dimensions and format.</p>
    <p><strong>Method</strong>: POST</p>
    <p><strong>Request URL</strong>: <code>/dimensions</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-enhance">POST /enhance </h3>
    <p><strong>Description</strong>: Enhance image by adjusting contrast and sharpness.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/enhance</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-emboss">POST /emboss </h3>
    <p><strong>Description</strong>: Apply emboss effect to image.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/emboss</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span>
    <span class="token punctuation">}</span>
    </code></pre><h3 id="post-reduce_colors">POST /reduce_colors </h3>
    <p><strong>Description</strong>: Reduce the number of colors in image.</p>
    <p><strong>Method</strong>: <code>POST</code></p>
    <p><strong>Request URL</strong>: <code>/reduce_colors</code></p>
    <p><strong>Request Body</strong>:</p>
    <pre data-role="codeBlock" data-info="json" class="language-json json"><code><span class="token punctuation">{</span>
      <span class="token property">"image"</span><span class="token operator">:</span> <span class="token string">"&lt;base64_image&gt;"</span><span class="token punctuation">,</span>
      <span class="token property">"num_colors"</span><span class="token operator">:</span> &lt;num_colors&gt;
    <span class="token punctuation">}</span>
    </code></pre>
          </div>
          
          
        
        
        
        
        
        
      
        </body></html>
    """
    return render_template_string(html_content)

@app.route('/resize', methods=['POST'])
def resize_image():
    if 'image' not in request.json or 'width' not in request.json or 'height' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    width = int(request.json['width'])
    height = int(request.json['height'])
    
    return handle_image_processing(request.json['image'], lambda img: img.resize((width, height)))

@app.route('/grayscale', methods=['POST'])
def grayscale_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    return handle_image_processing(request.json['image'], lambda img: img.convert("L"))

@app.route('/no_transparency', methods=['POST'])
def no_transparency_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, (0, 0), img if img.mode == 'RGBA' else img.convert('RGBA'))
            return background
        return img
    
    return handle_image_processing(request.json['image'], process)

@app.route('/sprite_txt', methods=['POST'])
def sprite_txt_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        img = img.convert('P', palette=Image.ADAPTIVE, colors=16)
        pixel_data = img.getdata()
        char_map = '0123456789ABCDEF'
        text_representation = "".join([char_map[pixel] + ('\n' if (index + 1) % img.width == 0 else '') for index, pixel in enumerate(pixel_data)])
        return text_representation
    
    try:
        image_base64 = request.json['image']
        image = decode_base64_image(image_base64)
        text_representation = process(image)
        return jsonify({'sprite': text_representation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/negative', methods=['POST'])
def negative_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, (0, 0), img if img.mode == 'RGBA' else img.convert('RGBA'))
            img = background
        return ImageOps.invert(img.convert('RGB'))
    
    return handle_image_processing(request.json['image'], process)

@app.route('/black_white', methods=['POST'])
def black_white_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    return handle_image_processing(request.json['image'], lambda img: img.convert("1"))

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.json or 'format' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    image_base64 = request.json['image']
    output_format = request.json['format'].upper()
    
    if output_format not in ['JPG', 'PNG', 'BMP', 'GIF']:
        return jsonify({'error': 'Invalid format'}), 400
    
    try:
        image = decode_base64_image(image_base64)
        
        if output_format == 'JPG':
            output_format = 'JPEG'
        
        converted_image_base64 = encode_image_to_base64_format(image, output_format)
        
        return jsonify({'converted_image': converted_image_base64})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dimensions', methods=['POST'])
def get_image_dimensions():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    try:
        image_base64 = request.json['image']
        image = decode_base64_image(image_base64)
        width, height = image.size
        image_format = image.format
        
        return jsonify({
            'width': width,
            'height': height,
            'format': image_format
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/enhance', methods=['POST'])
def enhance_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        enhancer = ImageEnhance.Sharpness(img)
        return enhancer.enhance(2)
    
    return handle_image_processing(request.json['image'], process)

@app.route('/emboss', methods=['POST'])
def emboss_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        return img.filter(ImageFilter.EMBOSS)
    
    return handle_image_processing(request.json['image'], process)

@app.route('/reduce_colors', methods=['POST'])
def reduce_colors_image():
    if 'image' not in request.json or 'num_colors' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    num_colors = int(request.json['num_colors'])
    
    def process(img):
        return img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    
    return handle_image_processing(request.json['image'], process)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))