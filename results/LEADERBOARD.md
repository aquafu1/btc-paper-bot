# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1423 windows, 36424 settled trades, 454 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 730 | 34.8 | 35.3 | $-465.63 | -6.4% | $534.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1765 | 38.9 | 39.2 | $-747.88 | -4.2% | $252.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3638 | 50.9 | 50.1 | $-1019.43 | -2.8% | $-19.43 | -1.7 | done | can't tell from luck |
| value_ev5 | 2666 | 40.7 | 41.1 | $-1222.32 | -4.6% | $-222.32 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 3057 | 49.3 | 49.3 | $-1478.56 | -4.8% | $-478.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3057 | 50.7 | 50.9 | $-1577.86 | -5.2% | $-577.86 | -2.9 | done | losing for real |
| trend_filter | 2162 | 48.6 | 50.3 | $-1883.07 | -8.7% | $-883.07 | -4.1 | done | losing for real |
| coinflip | 5237 | 50.1 | 50.0 | $-2200.81 | -4.2% | $-1200.81 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3638 | 49.1 | 50.2 | $-2237.09 | -6.1% | $-1237.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5237 | 50.1 | 51.3 | $-3252.85 | -6.2% | $-2252.85 | -4.6 | done | losing for real |
| always_up | 5237 | 48.0 | 49.3 | $-3621.88 | -6.9% | $-2621.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9216 | 48.1 | 48.8 | $-4912.37 |
| ETH | 9898 | 48.1 | 48.0 | $-5210.78 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
