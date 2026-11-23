# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1224 windows, 33511 settled trades, 445 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1600 | 38.8 | 39.2 | $-746.99 | -4.7% | $253.01 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3360 | 50.8 | 50.3 | $-1094.27 | -3.3% | $-94.27 | -1.9 | done | can't tell from luck |
| value_ev5 | 2420 | 40.5 | 41.1 | $-1182.22 | -4.9% | $-182.22 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2811 | 49.6 | 49.4 | $-1270.50 | -4.5% | $-270.50 | -2.4 | done | losing for real |
| trend_filter | 1983 | 48.8 | 50.5 | $-1670.71 | -8.4% | $-670.71 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2811 | 50.4 | 51.0 | $-1675.91 | -6.0% | $-675.91 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3360 | 49.2 | 50.2 | $-2060.86 | -6.1% | $-1060.86 | -3.6 | done | losing for real |
| coinflip | 4838 | 50.0 | 50.1 | $-2217.19 | -4.6% | $-1217.19 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4838 | 50.2 | 51.4 | $-2934.62 | -6.1% | $-1934.62 | -4.3 | done | losing for real |
| always_up | 4838 | 47.8 | 49.3 | $-3547.24 | -7.3% | $-2547.24 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7793 | 48.1 | 48.9 | $-4365.36 |
| ETH | 8408 | 48.1 | 48.3 | $-4894.37 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
