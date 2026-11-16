# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 501 windows, 13789 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 255 | 33.7 | 35.5 | $-229.21 | -9.0% | $770.79 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1172 | 51.0 | 49.9 | $-253.08 | -2.2% | $746.92 | -0.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1393 | 50.0 | 49.7 | $-523.33 | -3.8% | $476.67 | -1.4 | done | can't tell from luck |
| value_ev10 | 647 | 37.9 | 39.8 | $-550.56 | -8.5% | $449.44 | -1.8 | done | can't tell from luck |
| trend_filter | 810 | 49.6 | 50.8 | $-557.73 | -6.9% | $442.27 | -2.0 | done | losing for real |
| value_ev5 | 959 | 40.0 | 41.6 | $-713.93 | -7.4% | $286.07 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1393 | 50.0 | 51.5 | $-1013.77 | -7.3% | $-13.77 | -2.8 | done | losing for real |
| coinflip | 1996 | 50.1 | 50.7 | $-1054.61 | -5.3% | $-54.61 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1172 | 49.0 | 51.3 | $-1063.45 | -9.1% | $-63.45 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1996 | 49.7 | 51.6 | $-1493.51 | -7.5% | $-493.51 | -3.5 | done | losing for real |
| always_up | 1996 | 46.3 | 50.2 | $-2377.51 | -11.9% | $-1377.51 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3110 | 47.4 | 49.2 | $-2574.42 |
| ETH | 3449 | 48.0 | 48.7 | $-2311.43 |
| SOL | 3598 | 47.7 | 49.1 | $-2740.69 |
| XRP | 3632 | 48.3 | 48.8 | $-2204.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
