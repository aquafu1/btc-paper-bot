# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 426 windows, 11720 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 213 | 34.7 | 36.2 | $-164.42 | -7.7% | $835.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1001 | 50.5 | 50.0 | $-329.11 | -3.3% | $670.89 | -1.1 | done | can't tell from luck |
| value_ev10 | 548 | 39.2 | 40.3 | $-343.41 | -6.3% | $656.59 | -1.2 | done | can't tell from luck |
| trend_filter | 670 | 49.6 | 50.8 | $-441.66 | -6.6% | $558.34 | -1.8 | done | can't tell from luck |
| value_ev5 | 822 | 41.2 | 42.1 | $-470.65 | -5.7% | $529.35 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1187 | 49.1 | 50.0 | $-647.41 | -5.5% | $352.59 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1187 | 50.9 | 51.7 | $-686.65 | -5.8% | $313.35 | -2.1 | done | losing for real |
| coinflip | 1697 | 50.6 | 50.9 | $-731.14 | -4.3% | $268.86 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1001 | 49.5 | 51.8 | $-876.15 | -8.8% | $123.85 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1697 | 49.6 | 51.6 | $-1283.41 | -7.6% | $-283.41 | -3.2 | done | losing for real |
| always_up | 1697 | 46.1 | 50.6 | $-2122.70 | -12.5% | $-1122.70 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2656 | 47.6 | 49.4 | $-2026.96 |
| ETH | 2945 | 48.0 | 48.9 | $-1869.80 |
| SOL | 3036 | 47.7 | 49.4 | $-2464.74 |
| XRP | 3083 | 48.8 | 49.3 | $-1735.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
