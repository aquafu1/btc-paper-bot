# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1109 windows, 30675 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3095 | 51.2 | 50.4 | $-769.24 | -2.5% | $230.76 | -1.4 | done | can't tell from luck |
| value_ev10 | 1430 | 37.8 | 39.1 | $-960.15 | -6.7% | $39.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2602 | 49.8 | 49.4 | $-1048.51 | -4.0% | $-48.51 | -2.0 | done | losing for real |
| trend_filter | 1814 | 49.3 | 50.4 | $-1332.21 | -7.3% | $-332.21 | -3.2 | done | losing for real |
| value_ev5 | 2167 | 39.8 | 41.0 | $-1345.13 | -6.2% | $-345.13 | -2.4 | done | losing for real |
| coinflip | 4428 | 50.5 | 50.2 | $-1672.55 | -3.8% | $-672.55 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2602 | 50.2 | 51.1 | $-1729.36 | -6.6% | $-729.36 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3095 | 48.8 | 50.2 | $-2139.62 | -6.9% | $-1139.62 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4428 | 50.7 | 51.4 | $-2342.26 | -5.3% | $-1342.26 | -3.6 | done | losing for real |
| always_up | 4428 | 47.5 | 49.3 | $-3556.88 | -8.0% | $-2556.88 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7024 | 48.4 | 49.0 | $-3501.44 |
| ETH | 7596 | 48.1 | 48.4 | $-4583.05 |
| SOL | 7985 | 48.1 | 48.4 | $-4490.08 |
| XRP | 8070 | 48.2 | 48.2 | $-4711.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
