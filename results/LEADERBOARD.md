# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 320 windows, 8574 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 693 | 53.2 | 51.7 | $-84.25 | -1.2% | $915.75 | -0.3 | done | can't tell from luck |
| value_ev20 | 163 | 33.7 | 36.8 | $-212.09 | -13.0% | $787.91 | -1.3 | Sat 11:00 PM | too few trades (163/200) |
| reversal_15m_0.10pct | 852 | 52.7 | 51.9 | $-237.87 | -2.8% | $762.13 | -0.9 | done | can't tell from luck |
| value_ev10 | 413 | 37.8 | 40.5 | $-449.41 | -10.9% | $550.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 617 | 39.5 | 42.2 | $-649.40 | -10.5% | $350.60 | -2.3 | done | losing for real |
| trend_filter | 475 | 44.8 | 50.4 | $-725.25 | -15.3% | $274.75 | -3.4 | done | losing for real |
| momentum_60m_0.30pct | 693 | 46.8 | 49.9 | $-759.06 | -11.0% | $240.94 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 852 | 47.3 | 49.8 | $-780.68 | -9.2% | $219.32 | -2.7 | done | losing for real |
| coinflip | 1272 | 49.8 | 51.0 | $-814.99 | -6.4% | $185.01 | -2.4 | done | losing for real |
| always_up | 1272 | 47.6 | 50.5 | $-1244.51 | -9.8% | $-244.51 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 1272 | 48.3 | 51.4 | $-1267.86 | -10.0% | $-267.86 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1921 | 46.2 | 49.3 | $-2025.50 |
| ETH | 2152 | 46.7 | 48.8 | $-2148.18 |
| SOL | 2232 | 48.0 | 49.4 | $-1779.52 |
| XRP | 2269 | 48.7 | 49.2 | $-1272.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
