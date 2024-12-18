# API Documentation

**<a name="_toc000"></a>Índice**

1. [Server](#_toc015)
    1. [Server Configuration](#_toc014)
    1. [Image Processor APP](#_toc013)
1. [Endpoints](#_toc016)
    1. [API help](#_toc001)
    1. [Image Resize](#_toc002)
    1. [Image to Grayscale](#_toc003)
    1. [Image Remove Transparency](#_toc004)
    1. [Image to Sprite TXT](#_toc005)
    1. [Image Negative](#_toc006)
    1. [Image to Black and White](#_toc007)
    1. [Image Convert](#_toc008)
    1. [Image Dimension and Type](#_toc009)
    1. [Image Enhance](#_toc010)
    1. [Image Emboss](#_toc011)
    1. [Image Reduce Number Colors](#_toc012)

## <a name="_toc015"></a>Server[↩︎](#_toc000)

### <a name="_toc014"></a>Configuration[↩︎](#_toc000)

#### Python

[![Python](https://img.shields.io/badge/Python-3.12.6-brightgreen.svg?logo=python)](https://www.python.org/downloads/release/python-3126/)

#### PIP support

[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen.svg?logo=flask)](https://flask.palletsprojects.com) [![Flask-Cors](https://img.shields.io/badge/Flask_Cors-4.0.0-brightgreen.svg?logo=python)](https://flask-cors.readthedocs.io/en/latest/) [![Requests](https://img.shields.io/badge/requests-2.31.0-brightgreen.svg?logo=python)](https://requests.readthedocs.io/en/latest/) [![Pillow](https://img.shields.io/badge/Pillow-10.1.0-brightgreen.svg?logo=python)](https://pillow.readthedocs.io/en/latest/)

### <a name="_toc013"></a>Image Processor APP[↩︎](#_toc000)

**Description**: Flask API to process images.<br>**App**: `Image process.py`<br>**Sintaxe**:
```python
python "Image process.py"
```

## <a name="_toc016"></a>Endpoints[↩︎](#_toc000)

### <a name="_toc001"></a>GET /[↩︎](#_toc000)

**Description**: Home page (this help).<br>**Method**: `GET`<br>**Request URL**: `/`

### <a name="_toc002"></a>POST /resize[↩︎](#_toc000)

**Description**: Resize image.<br>**Method**: `POST`<br>**Request URL**: `/resize`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "width": <new_width>,
  "height": <new_height>
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/resize' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>",
>    "width": <new_width>,
>    "height": <new_height>
>}'
>```

### <a name="_toc003"></a>POST /grayscale[↩︎](#_toc000)

**Description**: Convert image to grayscale.<br>**Method**: `POST`<br>**Request URL**: `/grayscale`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/grayscale' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc004"></a>POST /no_transparency[↩︎](#_toc000)

**Description**: Remove transparency from image.<br>**Method**: `POST`<br>**Request URL**: `/no_transparency`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/no_transparency' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc005"></a>POST /sprite_txt[↩︎](#_toc000)

**Description**: Convert image to text representation.<br>**Method**: `POST`<br>**Request URL**: `/sprite_txt`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/sprite_txt' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc006"></a>POST /negative[↩︎](#_toc000)

**Description**: Convert image to negative.<br>**Method**: `POST`<br>**Request URL**: `/negative`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/negative' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc007"></a>POST /black_white[↩︎](#_toc000)

**Description**: Convert image to black and white.<br>**Method**: `POST`<br>**Request URL**: `/black_white`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/black_white' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc008"></a>POST /convert[↩︎](#_toc000)

**Description**: Convert image format.<br>**Method**: `POST`<br>**Request URL**: `/convert`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "format": "<new_format>"
}
```
> [!TIP]
>**Note**: `<new_format>` can be `JPG`, `PNG`, `BMP`, or `GIF`.

>**Example**:
>```python
>curl --location '<server>:<port>/convert' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>",
>    "format": "<new_format>"
>}'
>```

### <a name="_toc009"></a>POST /dimensions[↩︎](#_toc000)

**Description**: Get image dimensions and format.<br>**Method**: POST<br>**Request URL**: `/dimensions`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/dimensions' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc010"></a>POST /enhance[↩︎](#_toc000)

**Description**: Enhance image by adjusting contrast and sharpness.<br>**Method**: `POST`<br>**Request URL**: `/enhance`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/enhance' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc011"></a>POST /emboss[↩︎](#_toc000)

**Description**: Apply emboss effect to image.<br>**Method**: `POST`<br>**Request URL**: `/emboss`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/emboss' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>"
>}'
>```

### <a name="_toc012"></a>POST /reduce_colors[↩︎](#_toc000)

**Description**: Reduce the number of colors in image.<br>**Method**: `POST`<br>**Request URL**: `/reduce_colors`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "num_colors": <num_colors>
}
```
>**Example**:
>```python
>curl --location '<server>:<port>/reduce_colors' \
>--header 'Content-Type: application/json' \
>--data '{
>    "image": "<base64_image>",
>    "num_colors": <num_colors>
>}'
>```