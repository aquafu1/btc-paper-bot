# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 764 windows, 21068 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2154 | 51.4 | 50.6 | $-541.13 | -2.5% | $458.87 | -1.2 | done | can't tell from luck |
| value_ev10 | 962 | 37.9 | 39.1 | $-627.51 | -6.5% | $372.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1782 | 49.9 | 49.6 | $-688.46 | -3.9% | $311.54 | -1.6 | done | can't tell from luck |
| trend_filter | 1240 | 49.9 | 50.9 | $-785.43 | -6.3% | $214.57 | -2.3 | done | losing for real |
| value_ev5 | 1455 | 40.2 | 41.1 | $-833.92 | -5.7% | $166.08 | -1.8 | done | can't tell from luck |
| coinflip | 3048 | 50.4 | 50.3 | $-1182.98 | -3.9% | $-182.98 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1782 | 50.1 | 51.2 | $-1235.67 | -6.9% | $-235.67 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2154 | 48.6 | 50.2 | $-1547.49 | -7.2% | $-547.49 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3048 | 51.0 | 51.7 | $-1559.77 | -5.1% | $-559.77 | -2.9 | done | losing for real |
| always_up | 3048 | 47.1 | 49.6 | $-2808.84 | -9.2% | $-1808.84 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4780 | 48.2 | 49.1 | $-2897.41 |
| ETH | 5257 | 48.1 | 48.6 | $-3417.69 |
| SOL | 5483 | 48.0 | 48.6 | $-3262.01 |
| XRP | 5548 | 48.6 | 48.5 | $-2535.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
