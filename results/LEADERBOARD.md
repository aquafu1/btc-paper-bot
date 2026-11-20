# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 902 windows, 24897 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1139 | 38.3 | 39.1 | $-601.46 | -5.3% | $398.54 | -1.4 | done | can't tell from luck |
| value_ev5 | 1723 | 40.0 | 41.0 | $-979.22 | -5.7% | $20.78 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2105 | 49.7 | 49.8 | $-1037.80 | -4.9% | $-37.80 | -2.3 | done | losing for real |
| trend_filter | 1477 | 49.8 | 51.0 | $-1045.79 | -7.1% | $-45.79 | -2.8 | done | losing for real |
| reversal_15m_0.10pct | 2539 | 50.4 | 50.4 | $-1050.42 | -4.1% | $-50.42 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2105 | 50.3 | 50.9 | $-1275.90 | -6.1% | $-275.90 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2539 | 49.6 | 50.4 | $-1342.35 | -5.3% | $-342.35 | -2.7 | done | losing for real |
| coinflip | 3602 | 50.2 | 50.3 | $-1572.30 | -4.4% | $-572.30 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3602 | 51.2 | 51.7 | $-1629.02 | -4.5% | $-629.02 | -2.8 | done | losing for real |
| always_up | 3602 | 46.9 | 49.6 | $-3498.08 | -9.7% | $-2498.08 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5671 | 48.3 | 49.1 | $-2994.98 |
| ETH | 6193 | 48.2 | 48.5 | $-3734.51 |
| SOL | 6494 | 48.2 | 48.6 | $-3690.51 |
| XRP | 6539 | 48.3 | 48.5 | $-3713.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
