# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 88 windows, 2244 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 346 | 56.1 | 50.8 | $+241.47 | +7.0% | $1241.47 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 166 | 59.6 | 52.9 | $+167.15 | +10.1% | $1167.15 | +1.4 | Wed 5:30 PM | too few trades (166/200) |
| reversal_15m_0.10pct | 214 | 55.6 | 52.3 | $+88.15 | +4.1% | $1088.15 | +0.6 | done | can't tell from luck |
| value_ev10 | 117 | 41.9 | 40.1 | $-13.12 | -1.1% | $986.88 | -0.1 | Thu 4:30 AM | too few trades (117/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 6:15 PM | too few trades (44/200) |
| trend_filter | 124 | 46.8 | 48.7 | $-89.77 | -7.2% | $910.23 | -0.8 | Thu 2:30 AM | too few trades (124/200) |
| value_ev5 | 161 | 39.8 | 41.6 | $-138.55 | -8.6% | $861.45 | -1.0 | Wed 6:30 PM | too few trades (161/200) |
| coinflip | 346 | 49.7 | 51.6 | $-238.13 | -6.9% | $761.87 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 214 | 44.4 | 49.4 | $-279.52 | -13.1% | $720.48 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 166 | 40.4 | 48.8 | $-330.48 | -19.9% | $669.52 | -2.6 | Wed 5:30 PM | too few trades (166/200) |
| always_up | 346 | 46.2 | 50.2 | $-378.00 | -10.9% | $622.00 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 478 | 48.3 | 49.8 | $-114.79 |
| ETH | 540 | 46.9 | 48.6 | $-291.53 |
| SOL | 606 | 49.7 | 48.5 | $-244.19 |
| XRP | 620 | 49.4 | 48.7 | $-384.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
