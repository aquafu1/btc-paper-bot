# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 145 windows, 3640 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 249 | 61.4 | 53.1 | $+322.92 | +13.0% | $1322.92 | +2.2 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 350 | 56.9 | 52.2 | $+216.43 | +6.2% | $1216.43 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 573 | 52.5 | 51.4 | $-125.07 | -2.2% | $874.93 | -0.5 | done | can't tell from luck |
| value_ev20 | 71 | 29.6 | 36.8 | $-175.47 | -24.7% | $824.53 | -1.7 | Sun 3:45 AM | too few trades (71/200) |
| coinflip | 573 | 51.7 | 50.9 | $-199.84 | -3.5% | $800.16 | -0.9 | done | can't tell from luck |
| value_ev10 | 191 | 36.1 | 40.5 | $-295.28 | -15.5% | $704.72 | -1.9 | Thu 7:45 AM | too few trades (191/200) |
| trend_filter | 183 | 40.4 | 49.2 | $-384.07 | -21.0% | $615.93 | -2.9 | Thu 9:30 AM | too few trades (183/200) |
| value_ev5 | 278 | 37.4 | 42.2 | $-434.86 | -15.6% | $565.14 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 350 | 43.1 | 50.1 | $-591.75 | -16.9% | $408.25 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 249 | 38.6 | 49.1 | $-600.90 | -24.1% | $399.10 | -3.9 | done | losing for real |
| always_up | 573 | 46.4 | 49.9 | $-670.96 | -11.7% | $329.04 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 783 | 45.7 | 49.5 | $-838.25 |
| ETH | 895 | 45.0 | 48.7 | $-1073.81 |
| SOL | 960 | 48.3 | 48.8 | $-705.64 |
| XRP | 1002 | 50.4 | 49.1 | $-321.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
