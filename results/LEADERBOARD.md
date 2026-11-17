# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 572 windows, 15848 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1350 | 51.5 | 49.7 | $-168.07 | -1.2% | $831.93 | -0.5 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 920 | 50.9 | 51.1 | $-434.64 | -4.7% | $565.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 748 | 37.6 | 39.4 | $-691.32 | -9.2% | $308.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1609 | 50.8 | 51.0 | $-810.67 | -5.0% | $189.33 | -2.1 | done | losing for real |
| value_ev5 | 1113 | 39.7 | 41.3 | $-881.72 | -7.9% | $118.28 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1609 | 49.2 | 49.9 | $-904.55 | -5.6% | $95.45 | -2.3 | done | losing for real |
| coinflip | 2280 | 49.9 | 50.4 | $-1217.73 | -5.3% | $-217.73 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1350 | 48.5 | 51.2 | $-1379.87 | -10.2% | $-379.87 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2280 | 50.4 | 51.9 | $-1546.13 | -6.8% | $-546.13 | -3.4 | done | losing for real |
| always_up | 2280 | 47.0 | 49.9 | $-2301.70 | -10.1% | $-1301.70 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3585 | 47.7 | 49.3 | $-2700.56 |
| ETH | 3954 | 48.0 | 48.6 | $-2695.37 |
| SOL | 4130 | 47.8 | 48.7 | $-3072.05 |
| XRP | 4179 | 48.6 | 48.6 | $-2196.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
