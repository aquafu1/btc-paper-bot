# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 656 windows, 18133 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1534 | 50.6 | 49.7 | $-379.39 | -2.5% | $620.61 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1859 | 51.6 | 50.9 | $-510.60 | -2.7% | $489.40 | -1.2 | done | can't tell from luck |
| trend_filter | 1052 | 50.3 | 51.0 | $-587.23 | -5.6% | $412.77 | -1.9 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2616 | 50.1 | 50.5 | $-1190.22 | -4.5% | $-190.22 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1534 | 49.4 | 51.3 | $-1216.93 | -7.9% | $-216.93 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1859 | 48.4 | 50.0 | $-1295.71 | -7.0% | $-295.71 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2616 | 50.7 | 51.8 | $-1456.83 | -5.6% | $-456.83 | -2.9 | done | losing for real |
| always_up | 2616 | 47.5 | 49.7 | $-2194.08 | -8.4% | $-1194.08 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4114 | 48.3 | 49.3 | $-2500.06 |
| ETH | 4524 | 48.3 | 48.7 | $-2762.91 |
| SOL | 4718 | 48.1 | 48.8 | $-2868.82 |
| XRP | 4777 | 48.5 | 48.6 | $-2272.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
