# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 643 windows, 17782 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1501 | 50.9 | 49.6 | $-253.57 | -1.7% | $746.43 | -0.7 | done | can't tell from luck |
| value_ev20 | 334 | 34.1 | 35.3 | $-256.80 | -7.7% | $743.20 | -1.1 | done | can't tell from luck |
| trend_filter | 1027 | 50.3 | 50.8 | $-538.76 | -5.2% | $461.24 | -1.7 | done | can't tell from luck |
| value_ev10 | 820 | 38.4 | 39.5 | $-564.07 | -6.9% | $435.93 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1830 | 51.3 | 51.0 | $-641.77 | -3.5% | $358.23 | -1.5 | done | can't tell from luck |
| value_ev5 | 1241 | 40.9 | 41.4 | $-659.18 | -5.3% | $340.82 | -1.6 | done | can't tell from luck |
| coinflip | 2566 | 50.2 | 50.5 | $-1162.20 | -4.5% | $-162.20 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1830 | 48.7 | 50.0 | $-1180.30 | -6.4% | $-180.30 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1501 | 49.1 | 51.4 | $-1331.11 | -8.9% | $-331.11 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2566 | 50.7 | 51.7 | $-1388.47 | -5.4% | $-388.47 | -2.8 | done | losing for real |
| always_up | 2566 | 47.2 | 49.7 | $-2282.22 | -8.9% | $-1282.22 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4042 | 48.3 | 49.2 | $-2432.93 |
| ETH | 4451 | 48.2 | 48.7 | $-2690.86 |
| SOL | 4614 | 48.0 | 48.8 | $-2871.79 |
| XRP | 4675 | 48.5 | 48.5 | $-2262.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
