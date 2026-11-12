# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 136 windows, 3415 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 239 | 62.8 | 53.1 | $+374.09 | +15.7% | $1374.09 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 326 | 57.4 | 52.2 | $+242.03 | +7.4% | $1242.03 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 537 | 51.8 | 51.1 | $-159.69 | -3.0% | $840.31 | -0.7 | done | can't tell from luck |
| value_ev20 | 64 | 28.1 | 36.6 | $-164.84 | -25.8% | $835.16 | -1.7 | Sun 8:45 AM | too few trades (64/200) |
| coinflip | 537 | 51.6 | 51.0 | $-192.88 | -3.6% | $807.12 | -0.9 | done | can't tell from luck |
| value_ev10 | 180 | 36.7 | 40.5 | $-244.65 | -13.6% | $755.35 | -1.6 | Thu 7:45 AM | too few trades (180/200) |
| trend_filter | 172 | 40.1 | 49.0 | $-361.43 | -21.0% | $638.57 | -2.7 | Thu 9:30 AM | too few trades (172/200) |
| value_ev5 | 258 | 37.6 | 42.1 | $-375.00 | -14.5% | $625.00 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 326 | 42.6 | 50.0 | $-563.92 | -17.3% | $436.08 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 239 | 37.2 | 49.1 | $-627.49 | -26.3% | $372.51 | -4.1 | done | losing for real |
| always_up | 537 | 46.4 | 50.1 | $-635.45 | -11.8% | $364.55 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 728 | 45.2 | 49.5 | $-835.97 |
| ETH | 854 | 44.8 | 48.8 | $-1019.35 |
| SOL | 899 | 48.7 | 48.7 | $-569.30 |
| XRP | 934 | 50.2 | 49.0 | $-284.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
