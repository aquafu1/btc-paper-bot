# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 920 windows, 25413 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1160 | 38.2 | 39.1 | $-622.90 | -5.4% | $377.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2157 | 50.3 | 49.8 | $-820.40 | -3.8% | $179.60 | -1.8 | done | can't tell from luck |
| trend_filter | 1509 | 50.2 | 51.0 | $-981.60 | -6.5% | $18.40 | -2.6 | done | losing for real |
| value_ev5 | 1758 | 39.8 | 41.0 | $-1039.83 | -5.9% | $-39.83 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2589 | 50.5 | 50.5 | $-1066.42 | -4.1% | $-66.42 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2589 | 49.5 | 50.3 | $-1406.97 | -5.4% | $-406.97 | -2.8 | done | losing for real |
| coinflip | 3673 | 50.3 | 50.3 | $-1565.88 | -4.3% | $-565.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2157 | 49.7 | 50.9 | $-1569.26 | -7.3% | $-569.26 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3673 | 51.0 | 51.6 | $-1804.21 | -4.9% | $-804.21 | -3.1 | done | losing for real |
| always_up | 3673 | 46.7 | 49.7 | $-3771.63 | -10.3% | $-2771.63 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5785 | 48.2 | 49.1 | $-3310.73 |
| ETH | 6326 | 48.2 | 48.5 | $-3919.32 |
| SOL | 6627 | 48.2 | 48.6 | $-3851.95 |
| XRP | 6675 | 48.3 | 48.5 | $-3712.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
