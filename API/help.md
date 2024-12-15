# API Documentation

## Endpoints

### GET /

**Description**: Home page.<br>**Method**: `GET`<br>**Request URL**: `/`

### POST /resize

**Description**: Resize image.<br>**Method**: `POST`<br>**Request URL**: `/resize`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "width": <new_width>,
  "height": <new_height>
}
```

### POST /grayscale

**Description**: Convert image to grayscale.<br>**Method**: `POST`<br>**Request URL**: `/grayscale`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /no_transparency

**Description**: Remove transparency from image.<br>**Method**: `POST`<br>**Request URL**: `/no_transparency`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /sprite_txt

**Description**: Convert image to text representation.<br>**Method**: `POST`<br>**Request URL**: `/sprite_txt`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /negative

**Description**: Convert image to negative.<br>**Method**: `POST`<br>**Request URL**: `/negative`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /black_white

**Description**: Convert image to black and white.<br>**Method**: `POST`<br>**Request URL**: `/black_white`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /convert

**Description**: Convert image format.<br>**Method**: `POST`<br>**Request URL**: `/convert`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "format": "<new_format>"
}
```
> [!TIP]
>**Note**: `<new_format>` can be `JPG`, `PNG`, `BMP`, or `GIF`.

### POST /dimensions

**Description**: Get image dimensions and format.<br>**Method**: POST<br>**Request URL**: `/dimensions`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /enhance

**Description**: Enhance image by adjusting contrast and sharpness.<br>**Method**: `POST`<br>**Request URL**: `/enhance`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /emboss

**Description**: Apply emboss effect to image.<br>**Method**: `POST`<br>**Request URL**: `/emboss`<br>**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /reduce_colors

**Description**: Reduce the number of colors in image.<br>**Method**: `POST`<br>**Request URL**: `/reduce_colors`<br>**Request Body**:
```json
{
  "image": "<base64_image>",
  "num_colors": <num_colors>
}
```