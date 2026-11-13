# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 268 windows, 6996 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 689 | 55.2 | 52.3 | $+105.71 | +1.5% | $1105.71 | +0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 558 | 53.2 | 52.2 | $-126.75 | -2.3% | $873.25 | -0.6 | done | can't tell from luck |
| value_ev20 | 122 | 32.8 | 36.7 | $-171.51 | -14.1% | $828.49 | -1.2 | Sun 12:30 PM | too few trades (122/200) |
| value_ev10 | 333 | 36.6 | 40.7 | $-443.49 | -13.3% | $556.51 | -2.1 | done | losing for real |
| trend_filter | 363 | 45.7 | 50.2 | $-490.09 | -13.5% | $509.91 | -2.6 | done | losing for real |
| value_ev5 | 492 | 39.2 | 42.4 | $-559.86 | -11.4% | $440.14 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 558 | 46.8 | 49.7 | $-603.55 | -10.8% | $396.45 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 1064 | 49.8 | 51.4 | $-778.92 | -7.3% | $221.08 | -2.5 | done | losing for real |
| coinflip | 1064 | 49.2 | 50.9 | $-802.57 | -7.5% | $197.43 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 689 | 44.8 | 49.7 | $-944.67 | -13.7% | $55.33 | -3.7 | done | losing for real |
| always_up | 1064 | 47.7 | 50.2 | $-988.58 | -9.3% | $11.42 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1560 | 46.5 | 49.6 | $-1619.84 |
| ETH | 1748 | 46.7 | 49.0 | $-1760.36 |
| SOL | 1811 | 48.2 | 49.3 | $-1380.65 |
| XRP | 1877 | 48.7 | 49.2 | $-1043.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
