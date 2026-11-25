# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1421 windows, 36384 settled trades, 446 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 730 | 34.8 | 35.3 | $-465.63 | -6.4% | $534.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1763 | 39.0 | 39.2 | $-727.88 | -4.1% | $272.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3634 | 50.8 | 50.1 | $-1047.26 | -2.9% | $-47.26 | -1.7 | done | can't tell from luck |
| value_ev5 | 2663 | 40.7 | 41.1 | $-1192.32 | -4.5% | $-192.32 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3053 | 49.3 | 49.3 | $-1456.02 | -4.8% | $-456.02 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3053 | 50.7 | 50.9 | $-1587.92 | -5.2% | $-587.92 | -2.9 | done | losing for real |
| trend_filter | 2158 | 48.6 | 50.4 | $-1860.54 | -8.6% | $-860.54 | -4.1 | done | losing for real |
| coinflip | 5232 | 50.1 | 50.0 | $-2187.41 | -4.2% | $-1187.41 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3634 | 49.2 | 50.2 | $-2197.09 | -6.0% | $-1197.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5232 | 50.2 | 51.3 | $-3238.09 | -6.2% | $-2238.09 | -4.6 | done | losing for real |
| always_up | 5232 | 48.0 | 49.3 | $-3607.12 | -6.9% | $-2607.12 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9191 | 48.1 | 48.8 | $-4837.31 |
| ETH | 9883 | 48.1 | 48.0 | $-5145.75 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
