# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 123 windows, 3130 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 231 | 61.5 | 53.0 | $+318.69 | +13.8% | $1318.69 | +2.2 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 294 | 56.5 | 51.8 | $+196.59 | +6.7% | $1196.59 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 484 | 52.1 | 50.8 | $-75.46 | -1.6% | $924.54 | -0.4 | done | can't tell from luck |
| value_ev10 | 166 | 38.0 | 40.3 | $-174.30 | -10.5% | $825.70 | -1.2 | Thu 6:45 AM | too few trades (166/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 2:45 AM | too few trades (61/200) |
| coinflip | 484 | 50.2 | 51.0 | $-289.10 | -6.0% | $710.90 | -1.4 | done | can't tell from luck |
| value_ev5 | 235 | 37.9 | 41.9 | $-319.45 | -13.6% | $680.55 | -1.8 | done | can't tell from luck |
| trend_filter | 166 | 41.0 | 48.9 | $-320.28 | -19.3% | $679.72 | -2.5 | Thu 6:45 AM | too few trades (166/200) |
| momentum_15m_0.10pct | 294 | 43.5 | 50.3 | $-472.16 | -16.1% | $527.84 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 231 | 38.5 | 49.2 | $-547.49 | -23.7% | $452.51 | -3.6 | done | losing for real |
| always_up | 484 | 45.9 | 50.3 | $-622.30 | -12.9% | $377.70 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 673 | 44.9 | 49.4 | $-780.15 |
| ETH | 768 | 44.9 | 48.7 | $-868.19 |
| SOL | 832 | 48.4 | 48.6 | $-553.37 |
| XRP | 857 | 49.9 | 48.9 | $-286.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
