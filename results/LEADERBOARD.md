# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 880 windows, 24301 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 459 | 35.7 | 34.8 | $-79.37 | -1.7% | $920.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1116 | 38.4 | 39.1 | $-547.55 | -4.9% | $452.45 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2054 | 50.0 | 49.8 | $-849.16 | -4.1% | $150.84 | -1.9 | done | can't tell from luck |
| trend_filter | 1432 | 50.2 | 50.9 | $-909.44 | -6.4% | $90.56 | -2.5 | done | losing for real |
| value_ev5 | 1685 | 40.0 | 41.0 | $-954.77 | -5.7% | $45.23 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2481 | 50.5 | 50.4 | $-996.41 | -4.0% | $3.59 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2481 | 49.5 | 50.4 | $-1367.94 | -5.5% | $-367.94 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2054 | 50.0 | 50.9 | $-1394.99 | -6.8% | $-394.99 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3513 | 51.3 | 51.7 | $-1544.52 | -4.4% | $-544.52 | -2.7 | done | losing for real |
| coinflip | 3513 | 50.1 | 50.3 | $-1583.73 | -4.5% | $-583.73 | -2.7 | done | losing for real |
| always_up | 3513 | 46.9 | 49.6 | $-3409.84 | -9.7% | $-2409.84 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5547 | 48.3 | 49.1 | $-2997.17 |
| ETH | 6045 | 48.1 | 48.5 | $-3753.20 |
| SOL | 6340 | 48.3 | 48.5 | $-3463.95 |
| XRP | 6369 | 48.4 | 48.5 | $-3423.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
