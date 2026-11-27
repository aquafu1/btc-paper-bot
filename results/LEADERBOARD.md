# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1572 windows, 38373 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 800 | 34.5 | 35.3 | $-554.34 | -6.9% | $445.66 | -1.5 | done | can't tell from luck |
| value_ev10 | 1899 | 38.5 | 39.1 | $-946.75 | -5.0% | $53.25 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3796 | 50.9 | 50.0 | $-970.42 | -2.6% | $29.58 | -1.6 | done | can't tell from luck |
| value_ev5 | 2852 | 40.5 | 41.0 | $-1386.13 | -4.9% | $-386.13 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3183 | 51.0 | 50.9 | $-1493.91 | -4.7% | $-493.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3183 | 49.0 | 49.2 | $-1687.95 | -5.3% | $-687.95 | -3.0 | done | losing for real |
| trend_filter | 2262 | 48.5 | 50.3 | $-1981.52 | -8.8% | $-981.52 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3796 | 49.1 | 50.2 | $-2359.09 | -6.2% | $-1359.09 | -3.9 | done | losing for real |
| coinflip | 5534 | 49.9 | 49.9 | $-2413.88 | -4.4% | $-1413.88 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5534 | 50.1 | 51.3 | $-3488.45 | -6.3% | $-2488.45 | -4.8 | done | losing for real |
| always_up | 5534 | 48.2 | 49.2 | $-3557.18 | -6.4% | $-2557.18 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10131 | 47.9 | 48.6 | $-5710.03 |
| ETH | 10932 | 48.0 | 47.8 | $-5545.36 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
