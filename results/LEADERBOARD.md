# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1590 windows, 38597 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 813 | 34.6 | 35.1 | $-565.00 | -6.9% | $435.00 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3810 | 50.9 | 50.0 | $-971.14 | -2.5% | $28.86 | -1.6 | done | can't tell from luck |
| value_ev10 | 1920 | 38.5 | 39.0 | $-979.67 | -5.1% | $20.33 | -1.8 | done | can't tell from luck |
| value_ev5 | 2881 | 40.5 | 41.0 | $-1400.38 | -4.9% | $-400.38 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3191 | 51.0 | 50.9 | $-1488.92 | -4.7% | $-488.92 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3191 | 49.0 | 49.2 | $-1683.81 | -5.3% | $-683.81 | -3.0 | done | losing for real |
| trend_filter | 2268 | 48.5 | 50.4 | $-2004.92 | -8.8% | $-1004.92 | -4.3 | done | losing for real |
| coinflip | 5571 | 50.1 | 49.9 | $-2262.91 | -4.1% | $-1262.91 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3810 | 49.1 | 50.2 | $-2366.99 | -6.2% | $-1366.99 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5571 | 50.1 | 51.3 | $-3496.65 | -6.3% | $-2496.65 | -4.8 | done | losing for real |
| always_up | 5571 | 48.2 | 49.1 | $-3550.86 | -6.4% | $-2550.86 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10240 | 48.0 | 48.6 | $-5668.97 |
| ETH | 11047 | 48.0 | 47.7 | $-5518.05 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
