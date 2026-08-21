# OCR Bench

本目录存放 OCR 评测相关内容（题目、榜单数据等）。

* 评测说明与排行可直接以 Markdown 文件存放在本目录
* 如需发布到 GitHub Pages 站点：在 `scripts/sync_md.py` 的 `SYNC_CONFIG`
  中添加映射后推送，GitHub Actions（监听 `code/**` 与 `ocr/**`）会自动
  重新生成说明页与榜单数据
