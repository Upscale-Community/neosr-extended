# neosr

**neosr** is a framework for training real-world single-image super-resolution networks.

## installation

Requires Python 3.11 and CUDA =>11.8

```
git clone https://github.com/muslll/neosr
cd neosr
```
Install latest [Pytorch (=>2.1) and TorchVision](https://pytorch.org/get-started/locally/) (required).

Then install other dependencies via `pip`:

```
pip install -e .
```

Alternatively, use [**`poetry`**](https://python-poetry.org/docs/#installation) (*recommended on linux*):

```
poetry install && poetry add torch@latest torchvision@latest
```
Note: You must use `poetry shell` to enter the env after installation.

***(optional)*** If you want to convert your models ([convert.py](convert.py)), you need to following dependencies:

```
pip install onnx onnxruntime-gpu onnxconverter-common onnxsim
```

You can also install using poetry (*recommended on linux*):

```
poetry add onnx onnxruntime-gpu onnxconverter-common onnxsim
```

Please read the [**wiki tutorial**](https://github.com/muslll/neosr/wiki/Model-Conversion) for converting your models.

## quick start

Start training by running:

```
python train.py -opt options.yml
```
Where `options.yml` is a configuration file. Templates can be found in [options](options/).
Please read the wiki [Configuration Walkthrough](https://github.com/muslll/neosr/wiki/Configuration-Walkthrough) for an explanation of each option.

## features

### Currently included archs:

| arch                                                                                              | option                                 		    |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| **[ESRGAN](https://github.com/xinntao/ESRGAN)**                                                   | **`old_esrgan`**                                  |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)                                             | `esrgan`                               		    |
| [SRVGGNetCompact](https://github.com/XPixelGroup/BasicSR/blob/master/basicsr/archs/srvgg_arch.py) | `compact`                              		    |
| [SwinIR](https://github.com/JingyunLiang/SwinIR)                                                  | `swinir_small`, `swinir_medium`        		    |
| [HAT](https://github.com/XPixelGroup/HAT)                                                         | `hat_s`, `hat_m`, `hat_l`              		    |
| [OmniSR](https://github.com/Francis0625/Omni-SR)                                                  | `omnisr`                               		    |
| [SRFormer](https://github.com/HVision-NKU/SRFormer)                                               | `srformer_light`, `srformer_medium`    		    |
| [DAT](https://github.com/zhengchen1999/dat)                                                       | `dat_light`, `dat_small`, `dat_medium`, `dat_2`   |
| [DITN](https://github.com/yongliuy/DITN)							                                | `ditn`				     	      	            |
| [DCTLSA](https://github.com/zengkun301/DCTLSA)						                            | `dctlsa`						                    |
| [SPAN](https://github.com/hongyuanyu/SPAN)							                            | `span`						                    |
| [NLSAN](https://github.com/zengkun301/NLSAN)    				                                    | `nlsan_medium`, `nlsan_light`                     |
| [DWT](https://github.com/soobin419/DWT)         				                                    | `dwt`			                                    |
| [EDAT](https://github.com/soobin419/EDAT)       				                                    | `edat`, `edat_light`	                            |
| [CRAFT](https://github.com/AVC2-UESTC/CRAFT-SR) 				                                    | `craft`			                                |
| [Bicubic++](https://github.com/aselsan-research-imaging-team/bicubic-plusplus)                    | `bpp`, `bpp_l`		                            |
| [Real-CUGAN](https://github.com/bilibili/ailab)				                                    | `cugan`			                                |


### Arch Inference times with provided testscript, rtx 3060

| type                  | fps|
|-----------------------|---:|
| `bicubic ++`          |1.76|
| `compact`             |1.37|
| `span`                |0.92|
| `ditn`                |0.76|
| `omnisr`              |0.54|
| `swinir_small`        |0.49|
| `craft`               |0.49|
| `srformer_light`      |0.43|
| `nlsan_light`         |0.38|
| `dctlsa`              |0.35|
| `dat_light`           |0.35|
| `esrgan`              |0.18|
| `swinir_medium`       |0.13|
| `dwt_light`           |0.12|
| `dat_small`           |0.08|
| `dat_2`               |0.08|
| `dat_medium`          |0.07|

### Supported Discriminators:

| net                               				  | option 		        |
|-----------------------------------------------------------------|-----------------------------|
| U-Net SN 							  | `unet` 		        |
| [A2-FPN](https://github.com/lironui/A2-FPN)			  | `a2fpn`			|

### Supported Optimizers:

| optimizer                                                                 | option             |
|---------------------------------------------------------------------------|--------------------|
| [Adam](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html)   | `Adam` or `adam`   |
| [AdamW](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html) | `AdamW` or `adamw` |
| [Lion](https://arxiv.org/abs/2302.06675)                                  | `Lion` or `lion`   |
| [LAMB](https://arxiv.org/abs/1904.00962)                                  | `Lamb` or `lamb`   |
| [Adan](https://github.com/sail-sg/Adan)                                   | `Adan` or `adan`   |

### Supported models:

| model   | description                                                            | option    |
|---------|------------------------------------------------------------------------|-----------|
| Default | Base model, supports both Generator and Discriminator                  | `default` |
| OTF     | Builds on top of `default`, adding Real-ESRGAN on-the-fly degradations | `otf`     |

### Supported dataset loaders:

| loader                                          | option   |
|-------------------------------------------------|----------|
| Paired datasets                                 | `paired` |
| Single datasets (for inference, no GT required) | `single` |
| Real-ESRGAN on-the-fly degradation              | `otf`    |

### Supported losses:

| loss                                                                   | option               		     |
|------------------------------------------------------------------------|-------------------------------------------|
| L1 Loss                                                                | `L1Loss`, `l1`       		     |
| L2 Loss                                                                | `MSELoss`, `l2`      		     |
| Huber Loss                                                             | `HuberLoss`, `huber` 		     |
| Perceptual Loss                                                        | `perceptual_opt`, `PerceptualLoss`        |
| GAN                                                                    | `gan_opt`, `GANLoss`, `MultiScaleGANLoss` |
| YUV Color Loss                                                         | `color_opt`, `colorloss`                  |
| [LDL Loss](https://github.com/csjliang/LDL)                            | `ldl_opt`  			             |
| [Focal Frequency](https://github.com/EndlessSora/focal-frequency-loss) | `ff_opt`, `focalfrequencyloss`            |

## datasets

If you don't have a dataset, you can either download research datasets like [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/) or use one of the following.
- `nomos_uni` (*recommended*): universal dataset containing real photographs and anime images
- `nomos8k`: dataset with real photographs only
- `hfa2k`: anime dataset

These datasets have been tiled and manually curated across multiple sources, including DIV8K, Adobe-MIT 5k, RAISE, FFHQ, etc.

| dataset                  | num images       | meta_info                                                                                                    | download                                                                                             | sha256                                                           |
|--------------------------|------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| nomos_uni                | 2989 (512x512px) | [nomos_uni_metainfo.txt](https://drive.google.com/file/d/1e_pg5nxrk9P2gpDo7CsVc4f1xE7_DV8x/view?usp=sharing) | [GDrive (1.3GB)](https://drive.google.com/file/d/1LVS7i9J3mP9f2Qav2Z9i9vq3y2xsKxA_/view?usp=sharing) | 6403764c3062aa8aa6b842319502004aab931fcab228f85eb94f14f3a4c224b2 |
| nomos_uni (lmdb)         | 2989 (512x512px) | -                                                                                                            | [GDrive (1.3GB)](https://drive.google.com/file/d/1MHJCS4Zl3H5nihgpA_VVliziXnhJ3aU7/view?usp=sharing) | 596e64ec7a4d5b5a6d44e098b12c2eaf6951c68239ade3e0a1fcb914c4412788 |
| nomos_uni (LQ 4x)        | 2989 (512x512px) | [nomos_uni_metainfo.txt](https://drive.google.com/file/d/1e_pg5nxrk9P2gpDo7CsVc4f1xE7_DV8x/view?usp=sharing) | [GDrive (92MB)](https://drive.google.com/file/d/1uvMl8dG8-LXjCOEoO9Aiq5Q9rd_BIUw9/view?usp=sharing)  | c467e078d711f818a0148cfb097b3f60763363de5981bf7ea650dad246946920 |
| nomos_uni (LQ 4x - lmdb) | 2989 (512x512px) | -                                                                                                            | [GDrive (91MB)](https://drive.google.com/file/d/1h27AsZze_FFsAsf8eXupcqIZQHhvwa1y/view?usp=sharing)  | 1d770b2c6721c97bd2679db68f43a9f12d59a580e9cfeefd368db5a4fab0f0bb |
| nomos8k                  | 8492 (512x512px) | [nomos8k_metainfo.txt](https://drive.google.com/file/d/1XCK82vVOoy7rfSHS8bNXKJSdTEmsLjnG/view?usp=sharing)   | [GDrive (3.4GB)](https://drive.google.com/file/d/1ppTpi1-FQEBp908CxfnbI5Gc9PPMiP3l/view?usp=sharing) | 89724f4adb651e1c17ebee9e4b2526f2513c9b060bc3fe16b317bbe9cd8dd138 |
| hfa2k                    | 2568 (512x512px) | [hfa2k_metainfo.txt](https://drive.google.com/file/d/1X1EYSF4vjLzwckfkN-juzS9UBRI2HZky/view?usp=sharing)     | [GDrive (3.2GB)](https://drive.google.com/file/d/1PonJdHWwCtBdG4i1LwThm06t6RibnVu8/view?usp=sharing) | 3a3d2293a92fb60507ecd6dfacd636a21fd84b96f8f19f8c8a55ad63ca69037a |

*Note: these are not intended for use in academic research*.

### community datasets
These are datasets made by the upscaling community. More info can be found in the [Enhance Everything discord](https://discord.gg/cpAUpDK)

- `kim's 8k Dataset V2`: Video Game Dataset

- `FaceUp`: Curated version of [FFHQ](https://github.com/NVlabs/ffhq-dataset)

- `SSDIR`: Curated version of [LSDIR](https://data.vision.ee.ethz.ch/yawli/).

| dataset                                                | num images        | meta_info      | download                                                                                                   | sha256          |
|--------------------------------------------------------|-------------------|----------------|------------------------------------------------------------------------------------------------------------|-----------------|
| [@Kim2091](https://github.com/Kim2091)'s 8k Dataset V2 | 672 (7680x4320px) | -              | [GDrive (33.5GB)](https://drive.google.com/drive/folders/1z6-UFJPciU5ysTaRXUPTfC9QrqW517G6?usp=drive_link) | -               |
| [@Phhofm](https://github.com/Phhofm) FaceUp            | 10000 (512x512)   | -              | [GDrive (4GB)](https://drive.google.com/file/d/1WFY0siR_ERVSnE2p7ouiCfV3wQizpAKr/view)                     | -               |
| [@Phhofm](https://github.com/Phhofm) SSDIR             | 10000 (512x512)   | -              | [Gdrive (4.5GB)](https://drive.google.com/file/d/1FA8Q-T3xZ6_KA7SHYgoa6idIS7xpdrl4/view)                   | -               |

# resources

- [OpenModelDB](https://openmodeldb.info/)
- [chaiNNer](https://chainner.app/)
- [Training Guide](https://github.com/Sirosky/Upscale-Hub/wiki/%F0%9F%93%88-Training-a-Model-in-NeoSR) from [@Sirosky](https://github.com/Sirosky) 
- [Training Info](https://github.com/Kim2091/training-info) from [@Kim](https://github.com/Kim2091)

# support me

&#9749; Consider supporting me on [**KoFi**](https://ko-fi.com/muslll). &#9749;

## license and acknowledgements

Released under the [Apache license](license.txt).
This code was originally based on [BasicSR](https://github.com/XPixelGroup/BasicSR). See other licenses in [license/readme](license/readme.md).

Thanks to [victorca25/traiNNer](https://github.com/victorca25/traiNNer), [styler00dollar/Colab-traiNNer](https://github.com/styler00dollar/Colab-traiNNer/) and [timm](https://github.com/huggingface/pytorch-image-models) for providing helpful insights into some problems.

Thanks to contributors [@Phhofm](https://github.com/Phhofm), [@Sirosky](https://github.com/Sirosky), [@Kim2091](https://github.com/Kim2091) and [@terrainer](https://github.com/terrainer) for helping with tests and bug reporting. 

