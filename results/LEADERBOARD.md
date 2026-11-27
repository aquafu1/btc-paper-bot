# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1560 windows, 38233 settled trades, 431 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 793 | 34.4 | 35.2 | $-569.84 | -7.2% | $430.16 | -1.5 | done | can't tell from luck |
| value_ev10 | 1888 | 38.5 | 39.1 | $-990.54 | -5.2% | $9.46 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3785 | 50.9 | 50.0 | $-1002.20 | -2.6% | $-2.20 | -1.6 | done | can't tell from luck |
| value_ev5 | 2835 | 40.5 | 41.0 | $-1414.19 | -5.0% | $-414.19 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3180 | 50.9 | 50.9 | $-1521.86 | -4.8% | $-521.86 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3180 | 49.1 | 49.2 | $-1657.95 | -5.2% | $-657.95 | -2.9 | done | losing for real |
| trend_filter | 2257 | 48.6 | 50.3 | $-1931.52 | -8.6% | $-931.52 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3785 | 49.1 | 50.2 | $-2324.55 | -6.1% | $-1324.55 | -3.8 | done | losing for real |
| coinflip | 5510 | 50.0 | 49.9 | $-2363.07 | -4.3% | $-1363.07 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5510 | 50.2 | 51.3 | $-3390.75 | -6.2% | $-2390.75 | -4.7 | done | losing for real |
| always_up | 5510 | 48.2 | 49.2 | $-3539.65 | -6.4% | $-2539.65 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10068 | 48.0 | 48.6 | $-5644.56 |
| ETH | 10855 | 48.1 | 47.8 | $-5477.32 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
