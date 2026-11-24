# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1307 windows, 34783 settled trades, 413 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 685 | 34.3 | 35.3 | $-510.82 | -7.5% | $489.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1676 | 38.8 | 39.2 | $-777.85 | -4.6% | $222.15 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3489 | 50.8 | 50.2 | $-1031.87 | -3.0% | $-31.87 | -1.7 | done | can't tell from luck |
| value_ev5 | 2530 | 40.5 | 41.1 | $-1264.55 | -5.0% | $-264.55 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2919 | 49.4 | 49.4 | $-1375.03 | -4.7% | $-375.03 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2919 | 50.6 | 51.0 | $-1579.78 | -5.4% | $-579.78 | -3.0 | done | losing for real |
| trend_filter | 2064 | 48.8 | 50.5 | $-1722.09 | -8.3% | $-722.09 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3489 | 49.2 | 50.2 | $-2182.99 | -6.3% | $-1182.99 | -3.7 | done | losing for real |
| coinflip | 5004 | 50.0 | 50.1 | $-2259.10 | -4.5% | $-1259.10 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5004 | 50.4 | 51.4 | $-2908.62 | -5.8% | $-1908.62 | -4.2 | done | losing for real |
| always_up | 5004 | 47.9 | 49.3 | $-3613.67 | -7.2% | $-2613.67 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8409 | 48.0 | 48.8 | $-4893.07 |
| ETH | 9064 | 48.2 | 48.2 | $-4749.06 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
