# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 896 windows, 24727 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1137 | 38.3 | 39.1 | $-604.14 | -5.3% | $395.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2087 | 49.9 | 49.8 | $-955.33 | -4.6% | $44.67 | -2.1 | done | losing for real |
| trend_filter | 1460 | 50.1 | 51.0 | $-964.54 | -6.6% | $35.46 | -2.6 | done | losing for real |
| value_ev5 | 1718 | 39.9 | 41.0 | $-997.05 | -5.8% | $2.95 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2523 | 50.4 | 50.4 | $-1037.52 | -4.1% | $-37.52 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2087 | 50.1 | 50.8 | $-1352.90 | -6.5% | $-352.90 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2523 | 49.6 | 50.4 | $-1353.90 | -5.4% | $-353.90 | -2.7 | done | losing for real |
| coinflip | 3576 | 50.3 | 50.3 | $-1551.74 | -4.3% | $-551.74 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3576 | 51.4 | 51.7 | $-1561.43 | -4.4% | $-561.43 | -2.7 | done | losing for real |
| always_up | 3576 | 46.8 | 49.6 | $-3537.52 | -9.9% | $-2537.52 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5634 | 48.3 | 49.1 | $-2973.56 |
| ETH | 6152 | 48.3 | 48.5 | $-3722.68 |
| SOL | 6456 | 48.2 | 48.6 | $-3607.01 |
| XRP | 6485 | 48.3 | 48.5 | $-3714.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
