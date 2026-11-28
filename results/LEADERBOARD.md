# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1634 windows, 39164 settled trades, 354 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 833 | 34.5 | 35.2 | $-601.28 | -7.2% | $398.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3856 | 50.8 | 50.0 | $-1017.63 | -2.6% | $-17.63 | -1.6 | done | can't tell from luck |
| value_ev10 | 1965 | 38.4 | 39.0 | $-1085.91 | -5.5% | $-85.91 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3225 | 51.0 | 50.9 | $-1512.68 | -4.7% | $-512.68 | -2.7 | done | losing for real |
| value_ev5 | 2936 | 40.4 | 41.0 | $-1528.45 | -5.2% | $-528.45 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3225 | 49.0 | 49.2 | $-1731.86 | -5.4% | $-731.86 | -3.0 | done | losing for real |
| trend_filter | 2294 | 48.5 | 50.3 | $-2019.36 | -8.8% | $-1019.36 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3856 | 49.2 | 50.2 | $-2356.34 | -6.1% | $-1356.34 | -3.8 | done | losing for real |
| coinflip | 5658 | 50.0 | 49.9 | $-2397.47 | -4.2% | $-1397.47 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5658 | 50.2 | 51.3 | $-3485.84 | -6.2% | $-2485.84 | -4.8 | done | losing for real |
| always_up | 5658 | 48.3 | 49.1 | $-3508.63 | -6.2% | $-2508.63 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10489 | 48.0 | 48.6 | $-5816.94 |
| ETH | 11365 | 48.0 | 47.6 | $-5844.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
