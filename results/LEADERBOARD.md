# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 396 windows, 10872 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sat 11:45 PM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 922 | 50.5 | 49.8 | $-239.70 | -2.6% | $760.30 | -0.8 | done | can't tell from luck |
| value_ev5 | 767 | 42.1 | 42.2 | $-280.26 | -3.7% | $719.74 | -0.9 | done | can't tell from luck |
| trend_filter | 616 | 49.7 | 50.6 | $-352.65 | -5.7% | $647.35 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1094 | 49.2 | 49.8 | $-512.58 | -4.7% | $487.42 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1094 | 50.8 | 52.0 | $-672.37 | -6.1% | $327.63 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 922 | 49.5 | 52.1 | $-811.52 | -8.8% | $188.48 | -2.8 | done | losing for real |
| coinflip | 1580 | 50.0 | 50.8 | $-814.38 | -5.2% | $185.62 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1580 | 49.7 | 51.6 | $-1096.22 | -6.9% | $-96.22 | -2.9 | done | losing for real |
| always_up | 1580 | 46.3 | 50.8 | $-1914.00 | -12.1% | $-914.00 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2460 | 47.7 | 49.4 | $-1711.62 |
| ETH | 2727 | 48.0 | 48.9 | $-1672.06 |
| SOL | 2811 | 48.0 | 49.5 | $-2080.48 |
| XRP | 2874 | 48.9 | 49.2 | $-1450.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
