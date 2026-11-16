# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 552 windows, 15321 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1307 | 51.3 | 49.7 | $-228.15 | -1.7% | $771.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 302 | 33.4 | 35.2 | $-315.92 | -10.5% | $684.08 | -1.4 | done | can't tell from luck |
| trend_filter | 891 | 50.5 | 51.0 | $-489.63 | -5.5% | $510.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 726 | 37.2 | 39.3 | $-729.19 | -10.0% | $270.81 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1553 | 49.4 | 49.8 | $-811.16 | -5.2% | $188.84 | -2.1 | done | losing for real |
| value_ev5 | 1079 | 39.6 | 41.2 | $-892.47 | -8.3% | $107.53 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1553 | 50.6 | 51.2 | $-927.02 | -6.0% | $72.98 | -2.4 | done | losing for real |
| coinflip | 2201 | 50.0 | 50.5 | $-1224.47 | -5.6% | $-224.47 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1307 | 48.7 | 51.2 | $-1305.58 | -10.0% | $-305.58 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2201 | 50.2 | 51.8 | $-1602.52 | -7.3% | $-602.52 | -3.6 | done | losing for real |
| always_up | 2201 | 46.8 | 49.9 | $-2411.72 | -11.0% | $-1411.72 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3463 | 47.5 | 49.2 | $-2825.13 |
| ETH | 3816 | 47.9 | 48.6 | $-2746.73 |
| SOL | 3995 | 47.7 | 48.7 | $-3090.60 |
| XRP | 4047 | 48.5 | 48.6 | $-2275.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
