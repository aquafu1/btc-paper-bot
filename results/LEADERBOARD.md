# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 893 windows, 24657 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 462 | 35.7 | 34.9 | $-81.30 | -1.8% | $918.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1131 | 38.2 | 39.1 | $-619.52 | -5.5% | $380.48 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2082 | 49.9 | 49.8 | $-947.19 | -4.5% | $52.81 | -2.1 | done | losing for real |
| trend_filter | 1452 | 50.0 | 51.0 | $-990.12 | -6.8% | $9.88 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2518 | 50.5 | 50.4 | $-1016.12 | -4.0% | $-16.12 | -2.0 | done | losing for real |
| value_ev5 | 1711 | 39.9 | 41.0 | $-1024.05 | -6.0% | $-24.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2082 | 50.1 | 50.9 | $-1345.88 | -6.5% | $-345.88 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2518 | 49.5 | 50.4 | $-1374.45 | -5.5% | $-374.45 | -2.8 | done | losing for real |
| coinflip | 3567 | 50.3 | 50.3 | $-1535.41 | -4.3% | $-535.41 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3567 | 51.3 | 51.7 | $-1601.46 | -4.5% | $-601.46 | -2.8 | done | losing for real |
| always_up | 3567 | 46.9 | 49.6 | $-3490.49 | -9.8% | $-2490.49 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5621 | 48.3 | 49.1 | $-3012.25 |
| ETH | 6137 | 48.2 | 48.5 | $-3716.31 |
| SOL | 6432 | 48.2 | 48.6 | $-3680.94 |
| XRP | 6467 | 48.3 | 48.5 | $-3616.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
