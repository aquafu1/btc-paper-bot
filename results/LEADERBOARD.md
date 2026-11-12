# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 145 windows, 3631 settled trades, 77 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 248 | 61.7 | 53.1 | $+332.92 | +13.4% | $1332.92 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 349 | 57.0 | 52.2 | $+226.43 | +6.5% | $1226.43 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 572 | 52.4 | 51.4 | $-134.37 | -2.3% | $865.63 | -0.6 | done | can't tell from luck |
| value_ev20 | 71 | 29.6 | 36.8 | $-175.47 | -24.7% | $824.53 | -1.7 | Sun 3:00 AM | too few trades (71/200) |
| coinflip | 572 | 51.6 | 50.9 | $-209.14 | -3.7% | $790.86 | -0.9 | done | can't tell from luck |
| value_ev10 | 191 | 36.1 | 40.5 | $-295.28 | -15.5% | $704.72 | -1.9 | Thu 7:30 AM | too few trades (191/200) |
| trend_filter | 182 | 40.1 | 49.2 | $-393.37 | -21.6% | $606.63 | -2.9 | Thu 9:30 AM | too few trades (182/200) |
| value_ev5 | 277 | 37.2 | 42.1 | $-444.16 | -16.0% | $555.84 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 349 | 43.0 | 50.0 | $-601.05 | -17.2% | $398.95 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 248 | 38.3 | 49.1 | $-610.20 | -24.6% | $389.80 | -3.9 | done | losing for real |
| always_up | 572 | 46.5 | 49.9 | $-660.96 | -11.6% | $339.04 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 774 | 45.5 | 49.5 | $-864.05 |
| ETH | 895 | 45.0 | 48.7 | $-1073.81 |
| SOL | 960 | 48.3 | 48.8 | $-705.64 |
| XRP | 1002 | 50.4 | 49.1 | $-321.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
