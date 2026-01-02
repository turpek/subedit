

# Documentação Técnica: Mapeamento de Objetos MKV (Refinado)

Este documento mapeia a saída JSON do `mkvmerge --identify` para comandos CLI, organizado por estrutura de classes para facilitar a implementação de objetos em automação de software.

### Legenda de Colunas

- **Chave JSON:** Nome da propriedade no arquivo de identificação.
- **Tipo:** Tipo de dado (String, Integer, Boolean, etc.).
- **Flag mkvmerge:** Argumento para criação de arquivos (Remux).
- **Flag mkvpropedit:** Argumento para modificação in-place (sem remux).
- **Descrição Técnica:** Detalhes sobre a função do campo e discrepâncias de nomenclatura.

---

## 1. Classe: File (Container Global)

Representa o arquivo `.mkv` como um todo e suas propriedades de cabeçalho (Segment Info).

| Chave JSON (Property)   | Tipo    | Flag mkvmerge       | Flag mkvpropedit                      | Descrição Técnica                                                                   |
| ----------------------- | ------- | ------------------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| **file_name**           | String  | N/A (Entrada)       | `{arquivo}`                           | Caminho do arquivo. Somente leitura no JSON.                                        |
| **title**               | String  | `--title`           | `--edit info --set title="..."`       | Título global do filme/arquivo.                                                     |
| **date_local**          | String  | `--date`            | `--edit info --set date="..."`        | Data de muxing. **Nota:** No propedit, usa-se `date` direto, sem o sufixo `_local`. |
| **segment_uid**         | String  | `--segment-uid`     | `--edit info --set segment-uid="..."` | Identificador único de 128-bit do arquivo.                                          |
| **muxing_application**  | String  | N/A (Automático)    | N/A (Somente Leitura)                 | Biblioteca usada para criar o arquivo (ex: libebml).                                |
| **writing_application** | String  | N/A (Automático)    | N/A (Somente Leitura)                 | Aplicação usada para criar o arquivo (ex: mkvmerge v50).                            |
| **duration**            | Integer | N/A (Calculado)     | N/A (Somente Leitura)                 | Duração total em nanossegundos. Não editável diretamente.                           |
| **timestamp_scale**     | Integer | `--timestamp-scale` | N/A                                   | Escala base de tempo. Difícil edição sem remux.                                     |

---

## 2. Classe: Track (Superclasse)

Atributos comuns herdados por todas as trilhas (Vídeo, Áudio, Legenda). *Seletor mkvpropedit:* `--edit track:n` (onde `n` é o ID ou número).

| Chave JSON (Property)      | Tipo    | Flag mkvmerge              | Flag mkvpropedit                 | Descrição Técnica                                                  |
| -------------------------- | ------- | -------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| **id**                     | Integer | N/A                        | `--edit track:{id}`              | ID interno usado pelo mkvmerge para referenciar a trilha.          |
| **track_name**             | String  | `--track-name`             | `--set name="..."`               | **Discrepância:** JSON usa `track_name`, flags usam apenas `name`. |
| **language**               | String  | `--language`               | `--set language="..."`           | Código ISO 639-2 (ex: `por`).                                      |
| **language_ietf**          | String  | `--language`               | `--set language-ietf="..."`      | Código BCP 47 (ex: `pt-BR`).                                       |
| **default_track**          | Bool    | `--default-track-flag`     | `--set flag-default=0\           | 1`                                                                 |
| **forced_track**           | Bool    | `--forced-display-flag`    | `--set flag-forced=0\            | 1`                                                                 |
| **enabled_track**          | Bool    | `--track-enabled-flag`     | `--set flag-enabled=0\           | 1`                                                                 |
| **uid**                    | Integer | N/A                        | `--set track-uid="..."`          | ID único persistente da trilha.                                    |
| **codec**                  | String  | N/A                        | N/A                              | Nome legível do codec. Somente leitura.                            |
| **codec_id**               | String  | N/A                        | N/A                              | ID técnico (ex: `V_MPEG4/ISO/AVC`). Somente leitura.               |
| **default_duration**       | Integer | `--default-duration`       | `--set default-duration="..."`   | Define a duração do frame (FPS para vídeo).                        |
| **flag_hearing_impaired**  | Bool    | `--hearing-impaired-flag`  | `--set flag-hearing-impaired=0\  | 1`                                                                 |
| **flag_visual_impaired**   | Bool    | `--visual-impaired-flag`   | `--set flag-visual-impaired=0\   | 1`                                                                 |
| **flag_text_descriptions** | Bool    | `--text-descriptions-flag` | `--set flag-text-descriptions=0\ | 1`                                                                 |
| **flag_original**          | Bool    | `--original-flag`          | `--set flag-original=0\          | 1`                                                                 |
| **flag_commentary**        | Bool    | `--commentary-flag`        | `--set flag-commentary=0\        | 1`                                                                 |

---

## 3. Classe: Video (Subclasse de Track)

Propriedades exclusivas ou críticas para trilhas de vídeo.

| Chave JSON (Property)              | Tipo    | Flag mkvmerge                      | Flag mkvpropedit                                    | Descrição Técnica                                            |
| ---------------------------------- | ------- | ---------------------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| **display_dimensions**             | String  | `--display-dimensions`             | `--set display-width=...``--set display-height=...` | Formato `WxH`. Propedit altera largura/altura separadamente. |
| **pixel_dimensions**               | String  | N/A                                | N/A                                                 | Resolução codificada no bitstream. Somente leitura.          |
| **stereo_mode**                    | Integer | `--stereo-mode`                    | `--set stereo-mode=...`                             | Define modo 3D (ex: side-by-side).                           |
| **field_order**                    | Integer | `--field-order`                    | N/A                                                 | Ordem de entrelaçamento. Geralmente requer remux.            |
| **color_range**                    | Integer | `--color-range`                    | `--set color-range=...`                             | Alcance de cor (Full/Limited).                               |
| **color_primaries**                | Integer | `--color-primaries`                | `--set color-primaries=...`                         | Cores primárias (ex: BT.2020).                               |
| **color_transfer_characteristics** | Integer | `--color-transfer-characteristics` | `--set color-transfer-characteristics=...`          | Curva de transferência (Gamma/HDR).                          |
| **color_matrix_coefficients**      | Integer | `--color-matrix-coefficients`      | `--set color-matrix-coefficients=...`               | Matriz de coeficientes.                                      |

---

## 4. Classe: Audio (Subclasse de Track)

Propriedades exclusivas para trilhas de áudio.

| Chave JSON (Property)        | Tipo    | Flag mkvmerge      | Flag mkvpropedit | Descrição Técnica                                        |
| ---------------------------- | ------- | ------------------ | ---------------- | -------------------------------------------------------- |
| **audio_channels**           | Integer | N/A                | N/A              | Quantidade de canais. Definido no bitstream.             |
| **audio_sampling_frequency** | Integer | N/A                | N/A              | Taxa de amostragem (Hz). Definido no bitstream.          |
| **audio_bits_per_sample**    | Integer | N/A                | N/A              | Profundidade de bits. Definido no bitstream.             |
| **aac_is_sbr**               | Bool    | `--aac-is-sbr`     | N/A              | Flag específica para HE-AAC. Requer remux para correção. |
| **audio_emphasis**           | Integer | `--audio-emphasis` | N/A              | Ênfase de áudio. Requer remux.                           |

---

## 5. Classe: Subtitle (Subclasse de Track)

Propriedades exclusivas para legendas.

| Chave JSON (Property) | Tipo   | Flag mkvmerge   | Flag mkvpropedit | Descrição Técnica                                                                 |
| --------------------- | ------ | --------------- | ---------------- | --------------------------------------------------------------------------------- |
| **encoding**          | String | `--sub-charset` | N/A              | Charset da *entrada* (ex: converter CP1252 para UTF-8). Não editável após muxing. |
| **text_subtitles**    | Bool   | N/A             | N/A              | Informativo: Indica se a legenda é baseada em texto (SRT/ASS) ou imagem (PGS).    |

---

## 6. Classes de Suporte

### 6.1 Attachments (Anexos)

*Seletor mkvpropedit:* `--replace-attachment`, `--add-attachment` ou `--delete-attachment`.

| Chave JSON (Property) | Tipo    | Flag mkvmerge              | Flag mkvpropedit           | Descrição Técnica                                            |
| --------------------- | ------- | -------------------------- | -------------------------- | ------------------------------------------------------------ |
| **file_name**         | String  | `--attachment-name`        | `--attachment-name`        | Nome do arquivo armazenado dentro do MKV.                    |
| **content_type**      | String  | `--attachment-mime-type`   | `--attachment-mime-type`   | Tipo MIME (ex: `image/jpeg`, `application/x-truetype-font`). |
| **description**       | String  | `--attachment-description` | `--attachment-description` | Descrição legível do anexo.                                  |
| **uid**               | Integer | N/A                        | `--attachment-uid`         | ID único do anexo.                                           |

### 6.2 Chapters (Capítulos)

Tratados como um bloco único ou arquivo externo.

| Chave JSON (Property) | Tipo    | Flag mkvmerge | Flag mkvpropedit | Descrição Técnica                                    |
| --------------------- | ------- | ------------- | ---------------- | ---------------------------------------------------- |
| **num_entries**       | Integer | N/A           | N/A              | Contagem de capítulos (Informativo).                 |
| *(Objeto Completo)*   | XML     | `--chapters`  | `--chapters`     | Para editar, extrai-se XML, edita-se e reimporta-se. |

### 6.3 Tags

Metadados complexos.

| Chave JSON (Property) | Tipo  | Flag mkvmerge   | Flag mkvpropedit     | Descrição Técnica                    |
| --------------------- | ----- | --------------- | -------------------- | ------------------------------------ |
| **global_tags**       | Array | `--global-tags` | `--tags global:...`  | Tags que se aplicam ao arquivo todo. |
| **track_tags**        | Array | `--track-tags`  | `--tags track:n:...` | Tags específicas de uma trilha.      |

---

## 7. Lista de Exceções (Somente Leitura / Sem Flag Direta)

As seguintes chaves presentes no JSON `mkvmerge --identify` são informativas, derivadas do bitstream (dados brutos codificados) ou estatísticas geradas em tempo de execução, e portanto **não possuem flags diretas de edição** (embora algumas possam ser alteradas recodificando o arquivo):

1. **identification_format_version**: Versão do próprio JSON.
2. **container_type**: ID interno do MKVToolNix.
3. **recognized / supported**: Flags de capacidade do software.
4. **packetizer**: O módulo de software usado para processar a trilha.
5. **codec_private_data / codec_private_length**: Dados binários de inicialização do codec.
6. **pixel_dimensions / audio_channels / audio_sampling_frequency**: Propriedades físicas do stream comprimido.
7. **stream_id / sub_stream_id**: IDs originais do fluxo de transporte (ex: MPEG-TS).
8. **minimum_timestamp**: Dado estatístico.
9. **num_index_entries**: Dado estatístico de indexação (Cues).
