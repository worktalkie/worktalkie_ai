# Hugging Face 모델 다운로드 가이드

이 가이드는 Hugging Face에서 모델을 다운로드하고 `model/{모델명}` 폴더에 저장하는 방법을 설명합니다.

## 요구사항

1. **Git**: Hugging Face 모델 저장소를 클론하는 데 필요합니다.
2. **Git LFS (Large File Storage)**: Hugging Face에 있는 대용량 모델 파일을 처리하는 데 필요합니다.

### Git LFS 설치

먼저, Git LFS가 설치되어 있는지 확인하고, 설치되지 않았다면 아래 명령어를 사용하여 설치합니다.

- **macOS (Homebrew 사용):**

  ```bash
  brew install git-lfs
  ```

- **Ubuntu/Debian:**

  ```bash
  sudo apt-get install git-lfs
  ```

### Git LFS 초기화

Git LFS를 설치한 후, 아래 명령어로 Git LFS를 초기화합니다.

```bash
git lfs install
```

### Hugging Face 모델 다운로드

Hugging Face에서 모델을 클론하려면 다음 명령어를 사용하세요. `{모델명}`을 다운로드할 모델 이름으로 변경합니다. 기본적으로 'best_model.pth'를 추천합니다.

```bash
git clone https://huggingface.co/skush1/worktalkie-ai
```

### 모델을 `model/{모델명}` 폴더로 이동

다운로드한 모델 파일을 `model/{모델명}` 폴더로 이동합니다. `{모델명}`은 저장할 폴더 이름입니다.

```bash
mkdir -p model/{모델명}
mv worktalkie-ai/* model/{모델명}
```

### 완료

이제 모델이 `model/{모델명}` 폴더에 저장되었습니다. Hugging Face 모델을 사용할 준비가 되었습니다.