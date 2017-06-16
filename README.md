### Mac OS Text-to-speech (osxsay)

This TTS extension is based on the engine shipped with OSX and can be used with
[kalliope](https://github.com/kalliope-project/kalliope).

#### Installation

```bash
kalliope install --git-url "https://github.com/aleneum/kalliope-tts-osx.git"
```

#### Usage

| Parameters | Required | Default | Choices      | Comment                                         |
|------------|----------|---------|--------------|-------------------------------------------------|
| voice      | No       | Alex    | see below    | Voices also the define the used language        |
| rate       | No       | 175     | 1 to 1000    | Spoken words per minute                         |

A settings.yaml could look like this:

```yaml

text_to_speech:
  - osxsay:
      voice: "Alex"
      rate: 150
      cache: True

```

#### Supported voices

|   Voice   |  Language   |
|-----------|-------------|
| Alex      | en_US       |
| Alice     | it_IT       |
| Alva      | sv_SE       |
| Amelie    | fr_CA       |
| Anna      | de_DE       |
| Carmit    | he_IL       |
| Damayanti | id_ID       |
| Daniel    | en_GB       |
| Diego     | es_AR       |
| Ellen     | nl_BE       |
| Fiona     | en-scotland |
| Fred      | en_US       |
| Ioana     | ro_RO       |
| Joana     | pt_PT       |
| Jorge     | es_ES       |
| Juan      | es_MX       |
| Kanya     | th_TH       |
| Karen     | en_AU       |
| Kyoko     | ja_JP       |
| Laura     | sk_SK       |
| Lekha     | hi_IN       |
| Luca      | it_IT       |
| Luciana   | pt_BR       |
| Maged     | ar_SA       |
| Mariska   | hu_HU       |
| Mei-Jia   | zh_TW       |
| Melina    | el_GR       |
| Milena    | ru_RU       |
| Moira     | en_IE       |
| Monica    | es_ES       |
| Nora      | nb_NO       |
| Paulina   | es_MX       |
| Samantha  | en_US       |
| Sara      | da_DK       |
| Satu      | fi_FI       |
| Sin-ji    | zh_HK       |
| Tessa     | en_ZA       |
| Thomas    | fr_FR       |
| Ting-Ting | zh_CN       |
| Veena     | en_IN       |
| Victoria  | en_US       |
| Xander    | nl_NL       |
| Yelda     | tr_TR       |
| Yuna      | ko_KR       |
| Yuri      | ru_RU       |
| Zosia     | pl_PL       |
| Zuzana    | cs_CZ       |
