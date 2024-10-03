# CHIKV_HIPPO Scoring Criteria

510 recipes

- 50% ~€10k
- 50% <€30k

Best criteria for selection?

- num_products
- risk_diversity
- elaboration_balance

Performance:

- recipe.product_poses w/ temp table optimisation ~7mins
- inspiration_sets ~3mins
- interaction_count w/o optimisation ~19mins
- inspiration_balance ~3mins
- Scorer.scores ~16mins

# Scored scatter plots:

![num_prods_v_risk](https://github.com/user-attachments/assets/5e90159b-f611-4fbc-b92e-880e540dfea7)

# Individual attribute histograms:

## num_products (ok)

The number of product compounds in this selection

**suggests undersampling?**

![num_products](https://github.com/user-attachments/assets/a655bdbd-6ae2-4c51-8b08-d947bbf3a5a7)

## num_bases (bug?)

The number of Syndirella base compounds in this selection

![num_bases](https://github.com/user-attachments/assets/3c01c403-eff4-4145-b590-711323ba6ecf)

## num_bases_elaborated (ok)

**Most recipes have lots of series which is good**

![num_bases_elaborated](https://github.com/user-attachments/assets/6a5c03cd-26ec-401b-849f-b6723bd26b36)

## elaboration_balance (bimodal? bad performance?)

A measure for how evenly base compounds have been elaborated

**Bimodal distribution, better as a filter?**

![elaboration_balance](https://github.com/user-attachments/assets/652992d7-ed44-4123-a3c6-6eb6cb4f34fd)

## num_inspirations (flat, ignore)

**All sets have good number of inspirations**

The number of unique fragment compounds that inspired poses for product compounds in this selection

![num_inspirations](https://github.com/user-attachments/assets/561ffe6e-df20-4124-9b31-e068c66ace69)

## num_inspiration_sets (bad performance, skip)

**safe to ignore because of num_inspirations**

The number of unique fragment combinations that inspired poses for product compounds in this selection

## risk_diversity (ok, slow ~4mins)

A measure of how evenly spread the risk of elaborations are for each base compound. Risk in this case refers to the number of atoms added

![risk_diversity](https://github.com/user-attachments/assets/c90b3d29-54d0-42bb-8378-b6188eb16d9c)

## interaction_count (bad performance?)

**Needs performance review / optimisation**

The number of protein features that are being interacted with in this selection

## interaction_balance (bad performance?)

**Needs performance review / optimisation**

A measure for how evenly protein features are being interacted with in this selection

## num_subsites (review performance)

**Needs performance review / optimisation**

Count the number of subsites that poses in this set come into contact with

## subsite_balance (review performance)

**Needs performance review / optimisation**

Count the number of subsites that poses in this set come into contact with
