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

**Description**: Convert image to grayscale.
**Method**: `POST`
**Request URL**: `/grayscale`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /no_transparency

**Description**: Remove transparency from image.
**Method**: `POST`
**Request URL**: `/no_transparency`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /sprite_txt

**Description**: Convert image to text representation.
**Method**: `POST`
**Request URL**: `/sprite_txt`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /negative

**Description**: Convert image to negative.
**Method**: `POST`
**Request URL**: `/negative`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /black_white

**Description**: Convert image to black and white.
**Method**: `POST`
**Request URL**: `/black_white`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /convert

**Description**: Convert image format.
**Method**: `POST`
**Request URL**: `/convert`
**Request Body**:
```json
{
  "image": "<base64_image>",
  "format": "<new_format>"
}
```
> [!TIP]
>**Note**: `<new_format>` can be `JPG`, `PNG`, `BMP`, or `GIF`.

### POST /dimensions

**Description**: Get image dimensions and format.
**Method**: POST
**Request URL**: `/dimensions`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /enhance

**Description**: Enhance image by adjusting contrast and sharpness.
**Method**: `POST`
**Request URL**: `/enhance`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /emboss

**Description**: Apply emboss effect to image.
**Method**: `POST`
**Request URL**: `/emboss`
**Request Body**:
```json
{
  "image": "<base64_image>"
}
```

### POST /reduce_colors

**Description**: Reduce the number of colors in image.
**Method**: `POST`
**Request URL**: `/reduce_colors`
**Request Body**:
```json
{
  "image": "<base64_image>",
  "num_colors": <num_colors>
}
```