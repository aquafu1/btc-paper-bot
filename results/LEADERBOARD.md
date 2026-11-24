# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1302 windows, 34694 settled trades, 436 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 683 | 34.3 | 35.3 | $-516.32 | -7.6% | $483.68 | -1.5 | done | can't tell from luck |
| value_ev10 | 1672 | 38.8 | 39.2 | $-763.35 | -4.6% | $236.65 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3480 | 50.8 | 50.2 | $-1040.75 | -3.0% | $-40.75 | -1.8 | done | can't tell from luck |
| value_ev5 | 2523 | 40.5 | 41.1 | $-1220.05 | -4.8% | $-220.05 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2909 | 49.4 | 49.4 | $-1367.76 | -4.7% | $-367.76 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2909 | 50.6 | 51.0 | $-1560.87 | -5.4% | $-560.87 | -3.0 | done | losing for real |
| trend_filter | 2056 | 48.8 | 50.5 | $-1709.32 | -8.3% | $-709.32 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3480 | 49.2 | 50.3 | $-2150.77 | -6.2% | $-1150.77 | -3.7 | done | losing for real |
| coinflip | 4994 | 50.0 | 50.1 | $-2192.85 | -4.4% | $-1192.85 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4994 | 50.4 | 51.4 | $-2891.42 | -5.8% | $-1891.42 | -4.2 | done | losing for real |
| always_up | 4994 | 47.9 | 49.3 | $-3594.77 | -7.2% | $-2594.77 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8365 | 48.0 | 48.8 | $-4811.29 |
| ETH | 9019 | 48.3 | 48.2 | $-4612.70 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
