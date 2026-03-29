# solumn_coding

## Section A

### Question A

To assess the relationship between electrification and business performance, the data was aggregated to yearly regional level from 2018 to 2025. I then measured the correlation between `BEV_Share` and both `Units_Sold` and `Revenue_EUR` for each region.

#### Key findings
- All regions show a strong positive correlation between increasing `BEV_Share` and both sales volume and revenue.
- The USA has the strongest correlation:
  - Corr(BEV_Share, Units_Sold) ≈ 0.979
  - Corr(BEV_Share, Revenue_EUR) ≈ 0.981
- China shows the largest absolute increase in BEV share from 2018 to 2025:
  - 0.0202 → 0.1942, increase ≈ 0.1740
- Europe finishes with the highest BEV share in 2025:
  - ≈ 0.1950

#### Conclusion
The dataset suggests that higher BEV penetration is associated with stronger sales and revenue outcomes across all regions. The transition toward electrification is broadly consistent globally, with only small differences between regions. China shows the largest increase in BEV share, Europe ends with the highest final BEV share, and the USA shows the strongest positive relationship between BEV adoption and commercial performance.


### Question B

To estimate price elasticity, I applied a log-log regression between `Avg_Price_EUR` and `Units_Sold` for each model. The slope of this regression approximates price elasticity.

#### Key findings

- Several entry-level and mid-range models show high price elasticity (≈ -1 or lower), indicating strong sensitivity of demand to pricing changes.
- Premium and flagship models show significantly lower elasticity (closer to 0), suggesting that demand is less influenced by price and more by brand or product positioning.
- In some cases, slightly positive elasticity appears, which may reflect confounding factors such as product upgrades or market expansion rather than true causal effects.

#### Impact of economic conditions

- Under **low GDP growth**, models tend to exhibit higher elasticity, meaning consumers are more price-sensitive.
- Under **high GDP growth**, elasticity decreases, indicating stronger purchasing power and reduced sensitivity to price changes.

#### Conclusion

Price elasticity varies significantly across models:
- Entry-level models are more price-sensitive
- Premium models are more price-inelastic

Economic conditions further influence this relationship, with weaker economies amplifying price sensitivity.


### Question C

To analyze seasonality, I aggregated the dataset by month and examined average `Units_Sold` and `Revenue_EUR`.

#### Seasonal patterns

- Clear month-level patterns are observed across both sales and revenue.
- Demand tends to be lower in early months (January–February), increases mid-year, and peaks toward the end of the year (November–December).
- These patterns are consistent with typical automotive cycles, including promotional periods and year-end purchasing behavior.

#### Regional variation

- All regions exhibit similar seasonal structures, though the magnitude of fluctuations varies.
- Some regions show stronger peaks, suggesting localized market dynamics.

#### Interaction with economic indicators

- Under **low GDP growth**, seasonal effects are more pronounced, with sharper peaks and troughs.
- Under **high GDP growth**, demand is more stable across months, indicating reduced timing sensitivity.
- Fuel prices also influence patterns:
  - Higher fuel prices are associated with lower overall sales levels.
  - Lower fuel prices correspond to higher baseline demand.

#### Conclusion

Seasonality plays a significant role in both sales and revenue, with consistent global patterns. Economic conditions modulate these effects: weaker economies amplify seasonal fluctuations, while stronger economies stabilize demand. Fuel price variations further impact overall demand levels.