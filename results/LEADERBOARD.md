# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1555 windows, 38181 settled trades, 421 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 790 | 34.2 | 35.3 | $-633.30 | -8.0% | $366.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3783 | 50.9 | 50.0 | $-998.80 | -2.6% | $1.20 | -1.6 | done | can't tell from luck |
| value_ev10 | 1882 | 38.4 | 39.1 | $-1049.10 | -5.6% | $-49.10 | -2.0 | done | can't tell from luck |
| value_ev5 | 2828 | 40.4 | 41.0 | $-1462.75 | -5.2% | $-462.75 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3177 | 50.9 | 50.9 | $-1542.70 | -4.9% | $-542.70 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3177 | 49.1 | 49.2 | $-1645.05 | -5.2% | $-645.05 | -2.9 | done | losing for real |
| trend_filter | 2255 | 48.7 | 50.3 | $-1911.52 | -8.5% | $-911.52 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3783 | 49.1 | 50.2 | $-2324.05 | -6.1% | $-1324.05 | -3.8 | done | losing for real |
| coinflip | 5502 | 50.0 | 49.9 | $-2372.18 | -4.3% | $-1372.18 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5502 | 50.2 | 51.3 | $-3386.12 | -6.2% | $-2386.12 | -4.7 | done | losing for real |
| always_up | 5502 | 48.1 | 49.2 | $-3574.50 | -6.5% | $-2574.50 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10047 | 47.9 | 48.6 | $-5810.04 |
| ETH | 10824 | 48.1 | 47.8 | $-5505.80 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
