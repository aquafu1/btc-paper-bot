# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 461 windows, 12668 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 235 | 34.5 | 35.9 | $-180.67 | -7.7% | $819.33 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1074 | 50.9 | 50.0 | $-263.64 | -2.5% | $736.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 599 | 39.1 | 40.1 | $-371.87 | -6.2% | $628.13 | -1.3 | done | can't tell from luck |
| trend_filter | 733 | 49.8 | 50.7 | $-425.98 | -5.8% | $574.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 885 | 41.1 | 41.8 | $-485.25 | -5.5% | $514.75 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1280 | 49.8 | 50.0 | $-493.17 | -3.9% | $506.83 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1280 | 50.2 | 51.7 | $-917.85 | -7.2% | $82.15 | -2.7 | done | losing for real |
| coinflip | 1836 | 50.0 | 50.8 | $-993.43 | -5.4% | $6.57 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1074 | 49.1 | 51.8 | $-1026.20 | -9.6% | $-26.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1836 | 49.7 | 51.6 | $-1331.90 | -7.3% | $-331.90 | -3.2 | done | losing for real |
| always_up | 1836 | 46.2 | 50.4 | $-2238.91 | -12.2% | $-1238.91 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2866 | 47.6 | 49.2 | $-2204.85 |
| ETH | 3181 | 48.0 | 48.8 | $-2054.54 |
| SOL | 3298 | 47.7 | 49.3 | $-2550.86 |
| XRP | 3323 | 48.5 | 49.2 | $-1918.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
