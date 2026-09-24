# Transfermarkt API Guide

[![API Health Check](https://github.com/ethemdemirkaya/transfermarkt-api-guide/actions/workflows/health-check.yml/badge.svg)](https://github.com/ethemdemirkaya/transfermarkt-api-guide/actions/workflows/health-check.yml)
[![Deploy Docs](https://github.com/ethemdemirkaya/transfermarkt-api-guide/actions/workflows/docs.yml/badge.svg)](https://ethemdemirkaya.github.io/transfermarkt-api-guide/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

🇹🇷 Transfermarkt web sitesinin kullandığı gayriresmi (private) API endpoint'lerinin dökümantasyonu.
🇬🇧 Unofficial documentation of the private API endpoints used by the Transfermarkt website.

📖 **Web sitesi / Website:** https://ethemdemirkaya.github.io/transfermarkt-api-guide/

| | Dökümantasyon / Documentation |
|:-|:-|
| 🇹🇷 Türkçe | [docs/tr/index.md](docs/tr/index.md) |
| 🇬🇧 English | [docs/en/index.md](docs/en/index.md) |

> ⚠️ Bu proje Transfermarkt ile resmi olarak ilişkili değildir. Kullanmadan önce dökümandaki uyarıları okuyun.
> This project is not affiliated with Transfermarkt. Read the disclaimer in the docs before use.

## Endpoint Sağlık Kontrolü / Endpoint Health Check

Dökümante edilen endpoint'ler her pazartesi [GitHub Actions](.github/workflows/health-check.yml) ile otomatik test edilir. Yukarıdaki rozet kırmızıysa en az bir endpoint yanıt vermiyordur; hangisinin bozulduğunu son çalıştırmanın özetinde görebilirsiniz. Test edilen URL'ler [scripts/endpoints.json](scripts/endpoints.json) dosyasındadır.

Documented endpoints are tested automatically every Monday via GitHub Actions. A red badge means at least one endpoint is failing; the latest run's summary shows which one.

```bash
python scripts/health_check.py
```

## Yerelde Çalıştırma / Local Preview

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## Lisans / License

[MIT](LICENSE)
