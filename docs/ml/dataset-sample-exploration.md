# Team 3: Dataset Sample Exploration

## 1.0 Objective

This exploration is intended to validate the actual structure and usefulness of the RSVQA and VRSBench datasets before committing to larger-scale experiments. Understanding the precise image formats, annotation structures, and the availability of spatial grounding in these datasets is crucial for SatQuery AI's vision-language assistant capabilities.

## 2.0 RSVQA Sample Exploration

- **Dataset purpose:** Remote Sensing Visual Question Answering.
- **Source/access location:** Attempted access via official GitHub repository (https://github.com/syvlo/RSVQA) and Hugging Face.
- **Files inspected:** Attempted to download JSON annotation files (`RSVQA_LR_split_val_questions.json`) via curl and load via Hugging Face `datasets` library.
- **Sample size actually inspected:** 0
- **Image characteristics observed:** Unable to observe directly.
- **Annotation structure:** Unable to observe directly.
- **Example question types:** Unable to extract direct examples.
- **Example answer types:** Unable to extract direct examples.
- **Grounding availability:** Unable to confirm directly from samples (though literature suggests RSVQA lacks spatial bounding boxes).
- **Observed strengths:** Cannot be verified experimentally at this moment.
- **Observed limitations:** The dataset annotations are not easily accessible through direct public raw links or the standard Hugging Face datasets hub without additional authentication or locating the correct canonical URLs.
- **Relevance to SatQuery AI:** Still theoretically highly relevant for baseline VQA, but the data acquisition pipeline requires a more robust setup.

## 3.0 VRSBench Sample Exploration

- **Dataset purpose:** Versatile Vision-Language Benchmark for Remote Sensing (VQA, captioning, and visual grounding).
- **Source/access location:** Attempted access via Hugging Face (`xiang709/VRSBench`) and official GitHub repository (https://github.com/lx709/VRSBench).
- **Files inspected:** Attempted streaming via Hugging Face `datasets` and direct JSON download (`vrsbench_train.json`).
- **Sample size actually inspected:** 0
- **Image characteristics observed:** Unable to observe directly.
- **Annotation structure:** Unable to observe directly.
- **VQA structure:** Unable to observe directly.
- **Grounding/referring-expression structure:** Unable to observe directly (literature states it includes bounding boxes).
- **Observed strengths:** Cannot be verified experimentally at this moment.
- **Observed limitations:** Data extraction failed. Hugging Face datasets installation stalled due to Python environment constraints (e.g., extremely slow binary compilations/downloads), and direct API requests to the Hugging Face dataset server returned HTTP 500 errors. Direct GitHub raw links returned 404 Not Found.
- **Relevance to SatQuery AI:** Theoretically critical for the spatial grounding requirement, but data access paths must be fixed.

## 4.0 Comparative Assessment

| Aspect | RSVQA | VRSBench |
|--------|-------|----------|
| VQA | *Not directly verified (access failed)* | *Not directly verified (access failed)* |
| Spatial grounding | *Not directly verified* | *Not directly verified* |
| Question diversity | *Not directly verified* | *Not directly verified* |
| Annotation richness | *Not directly verified* | *Not directly verified* |
| Relevance to SatQuery | Expected high relevance for basic VQA | Expected critical relevance for grounding |
| Expected project use | Baseline model adaptation | Grounding model adaptation |

*(Note: The table reflects that direct observation was prevented by access limitations.)*

## 5.0 SatQuery AI Implications

The inability to quickly fetch and parse the dataset annotations implies the following for SatQuery AI:
- **VQA & Spatial Reasoning:** We cannot yet map the exact schema of the questions to our required agent capabilities. We need the actual data schema to build our dataloaders.
- **Grounding:** Without confirming how VRSBench represents spatial bounding boxes (e.g., absolute pixels vs relative coordinates), we cannot design the downstream prompt format.
- **Future model adaptation:** Data preprocessing scripts will be delayed until the access issue is resolved.
- **Evaluation:** We must ensure we have a stable, reproducible way to download the test splits. Relying on raw GitHub links or standard unauthenticated Hugging Face streams proved unreliable.

## 6.0 Recommended Next Step

**Recommended Action:** Resolve the Dataset Access & Preprocessing Pipeline.

Since the immediate attempt to explore RSVQA and VRSBench failed due to environment (slow pip compilations) and network/URL (404/500 errors) issues, the immediate next step must be to establish a robust dataset downloading script. We should investigate using authenticated Hugging Face Hub tokens or downloading the zipped archives directly from the authors' provided Zenodo/Google Drive links. 
Alternatively, we can proceed to **BigEarthNet.txt dataloader** implementation, assuming that dataset is already staged or more easily accessible.

## 7.0 Current Status

### COMPLETED
- RSVQA sample exploration (Attempted, documented failure)
- VRSBench sample exploration (Attempted, documented failure)
- documentation

### PENDING
- Resolving data access for RSVQA and VRSBench
- BigEarthNet.txt dataloader
- quantitative experiments
- model selection
- multitemporal exploration
- optical-SAR fusion experiments

## 8.0 Exploration Evidence

- **Exact files inspected:** None successfully loaded. Attempted `RSVQA_LR_split_val_questions.json` and `vrsbench_train.json`.
- **Approximate number of samples inspected:** 0
- **Commands/scripts used:** 
  1. Python `datasets` streaming script (`load_dataset("xiang709/VRSBench", streaming=True)`).
  2. Direct Hugging Face API call (`https://datasets-server.huggingface.co/rows?dataset=xiang709%2FVRSBench...`).
  3. Direct curl commands to GitHub raw content URLs.
- **Dataset source URLs:** 
  - https://github.com/syvlo/RSVQA
  - https://github.com/lx709/VRSBench
  - https://huggingface.co/datasets/xiang709/VRSBench
- **Date of exploration:** 2026-09-15
- **Limitations encountered:** 
  - Python `datasets` and `pyarrow` installation hung/was excessively slow in the `.venv`.
  - The Hugging Face dataset server API returned `status code 500`.
  - Direct raw GitHub URLs to expected JSON files returned `404: Not Found`.
