
## ewwink/tinymce-combined

TinyMCE and Plugins Combined into one js file, it uses Github Actions to pull and combine the files from

```
https://www.jsdelivr.com/package/npm/tinymce
```
The Actions check new version of TinyMCE every day (daily cronjob)

## Use it
```html
<link href="https://cdn.jsdelivr.net/gh/ewwink/tinymce-combined@latest/dist/skins/ui/oxide/content.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/gh/ewwink/tinymce-combined@latest/dist/tinymce-combined.min.js"></script>

or use specific version

<link href="https://cdn.jsdelivr.net/gh/ewwink/tinymce-combined@8.3.1/dist/skins/ui/oxide/content.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/gh/ewwink/tinymce-combined@8.3.1/dist/tinymce-combined.min.js"></script>
```

## Version

included JS and Plugin file in `tinymce-combined-standard`:

- tinymce.min.js
- themes/silver/theme.min.js
- models/dom/model.min.js
- icons/default/icons.min.js
- advlist
- anchor
- autolink
- charmap
- code
- fullscreen
- image
- link
- lists
- media
- preview
- searchreplace
- table
- visualblocks
- wordcount
- 

  
<img  width="931"  height="615"  alt="TinyMCE Combined"  src="https://github.com/user-attachments/assets/f9d3b3f5-b5af-4590-a0e0-b28a0842d3e7" />