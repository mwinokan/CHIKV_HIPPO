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

![newplot-55](https://github.com/user-attachments/assets/d1af1e2c-2619-4178-9f5d-d12f22afdb6b)

## num_bases (bug?, SKIP)

The number of Syndirella base compounds in this selection

![newplot-56](https://github.com/user-attachments/assets/ddd61ba4-dc94-4f93-b1b1-5d7cdb2b5a52)

## num_bases_elaborated (ok)

**Most recipes have lots of series which is good**

![newplot-57](https://github.com/user-attachments/assets/3ee81660-8c5b-44e5-8f46-c294df786296)


## elaboration_balance (bimodal? bad performance?)

A measure for how evenly base compounds have been elaborated

**Bimodal distribution, better as a filter?**

![newplot-58](https://github.com/user-attachments/assets/36c8ed02-3c97-4d66-a483-d13b51d49c2b)

## num_inspirations (flat, ignore)

**All sets have good number of inspirations**

The number of unique fragment compounds that inspired poses for product compounds in this selection

![newplot-59](https://github.com/user-attachments/assets/fef80714-e8e8-4f04-91ac-95926f454241)

## num_inspiration_sets (bad performance, skip)

**safe to ignore because of num_inspirations**

The number of unique fragment combinations that inspired poses for product compounds in this selection

![newplot-60](https://github.com/user-attachments/assets/992df1f0-b2fc-4229-906a-abb0881031d6)

## risk_diversity (ok, slow ~4mins)

A measure of how evenly spread the risk of elaborations are for each base compound. Risk in this case refers to the number of atoms added

![newplot-61](https://github.com/user-attachments/assets/295934c4-0e80-427a-b460-e82ecc1936ab)

## interaction_count (bad performance?)

**Needs performance review / optimisation**

The number of protein features that are being interacted with in this selection

![newplot-62](https://github.com/user-attachments/assets/cf22b3dc-54c7-46ed-a3db-d62a7c9374da)

## interaction_balance (bad performance?)

**Needs performance review / optimisation**

A measure for how evenly protein features are being interacted with in this selection

![newplot-63](https://github.com/user-attachments/assets/6d52b387-2f65-4086-baed-384388d160a9)

## num_subsites (review performance)

**Needs performance review / optimisation**

Count the number of subsites that poses in this set come into contact with

![newplot-64](https://github.com/user-attachments/assets/4386a5e6-56ed-41d8-b27c-4c1399f77bc2)

## subsite_balance (review performance)

**Needs performance review / optimisation**

A measure of how evenly subsites are populated

![newplot-65](https://github.com/user-attachments/assets/579a79a1-c163-48b7-a246-094698f5dff6)
